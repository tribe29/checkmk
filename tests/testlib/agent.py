#!/usr/bin/env python3
# Copyright (C) 2023 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import contextlib
import json
import logging
import os
import re
import subprocess
import time
from collections.abc import Iterator, Mapping
from pathlib import Path
from typing import Any

from tests.testlib.repo import repo_path
from tests.testlib.site import Site
from tests.testlib.utils import execute, run, wait_until

from cmk.utils.hostaddress import HostName

logger = logging.getLogger(__name__)

OMD_STATUS_CACHE = Path("/var/lib/check_mk_agent/cache/omd_status.cache")


def get_package_type() -> str:
    if os.path.exists("/var/lib/dpkg/status"):
        return "linux_deb"
    if (
        os.path.exists("/var/lib/rpm")
        and os.path.exists("/bin/rpm")
        or os.path.exists("/usr/bin/rpm")
    ):
        return "linux_rpm"
    raise NotImplementedError(
        "package_type recognition for the current environment is not supported yet. Please"
        " implement it if needed"
    )


def install_agent_package(package_path: Path) -> Path:
    package_type = get_package_type()
    installed_ctl_path = Path("/usr/bin/cmk-agent-ctl")
    if package_type == "linux_deb":
        try:
            run(["dpkg", "-i", package_path.as_posix()], sudo=True)
        except RuntimeError as e:
            process_table = run(["ps", "aux"]).stdout
            raise RuntimeError(f"dpkg failed. Process table:\n{process_table}") from e
        return installed_ctl_path
    if package_type == "linux_rpm":
        run(["rpm", "-vU", "--oldpackage", "--replacepkgs", package_path.as_posix()], sudo=True)
        return installed_ctl_path
    raise NotImplementedError(
        f"Installation of package type {package_type} is not supported yet, please implement it"
    )


def download_and_install_agent_package(site: Site, tmp_dir: Path) -> Path:
    if site.version.is_raw_edition():
        agent_download_resp = site.openapi.get(
            "domain-types/agent/actions/download/invoke",
            params={
                "os_type": get_package_type(),
            },
            headers={"Accept": "application/octet-stream"},
        )
    else:
        agent_download_resp = site.openapi.get(
            "domain-types/agent/actions/download_by_host/invoke",
            params={
                "agent_type": "generic",
                "os_type": get_package_type(),
            },
            headers={"Accept": "application/octet-stream"},
        )
    assert agent_download_resp.ok

    path_agent_package = tmp_dir / ("agent." + get_package_type())
    with path_agent_package.open(mode="wb") as tmp_agent_package:
        for chunk in agent_download_resp.iter_content(chunk_size=None):
            tmp_agent_package.write(chunk)

    return install_agent_package(path_agent_package)


def _is_containerized() -> bool:
    return (
        os.path.exists("/.dockerenv")
        or os.path.exists("/run/.containerenv")
        or os.environ.get("CMK_CONTAINERIZED") == "TRUE"
    )


@contextlib.contextmanager
def agent_controller_daemon(ctl_path: Path) -> Iterator[subprocess.Popen | None]:
    """Manually take over systemds job if we are in a container (where we have no systemd)."""
    if not _is_containerized():
        yield None
        return

    daemon_path = str(repo_path() / "tests" / "scripts" / "agent_controller_daemon.py")

    with execute(["python3", daemon_path, ctl_path.as_posix()], sudo=True) as daemon:
        yield daemon
    logger.info("Running agent controller daemon...")
    with execute([daemon_path], sudo=True) as daemon:
        # wait for a dump being returned successfully (may not work immediately after starting the agent controller)
        wait_until(
            lambda: execute([ctl_path.as_posix(), "dump"], sudo=True).wait() == 0,
            timeout=3,
            interval=0.1,
        )
        try:
            yield daemon
        finally:
            assert daemon.returncode is None, "Daemon was killed unexpectedly!"
            logger.info("Killing agent controller daemon...")
            daemon.kill()
            logger.info("daemon.stdout: %s", daemon.stdout)
            logger.info("daemon.stderr: %s", daemon.stderr)


def register_controller(
    ctl_path: Path, site: Site, hostname: HostName, site_address: str | None = None
) -> None:
    # first we delete all registrations to have a sane default state
    run(
        [
            ctl_path.as_posix(),
            "delete-all",
        ],
        sudo=True,
    )
    run(
        [
            ctl_path.as_posix(),
            "--verbose",
            "register",
            "--server",
            site_address if site_address else site.http_address,
            "--site",
            site.id,
            "--hostname",
            hostname,
            "--user",
            "cmkadmin",
            "--password",
            site.admin_password,
            "--trust-cert",
        ],
        sudo=True,
    )


def wait_until_host_receives_data(
    site: Site,
    hostname: HostName,
    *,
    timeout: int = 120,
    interval: int = 20,
) -> None:
    try:
        wait_until(
            lambda: not site.execute(
                ["cmk", "-d", hostname],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).wait(),
            timeout=timeout,
            interval=interval,
        )
    except TimeoutError as e:
        proc = site.execute(
            ["cmk", "-d", hostname],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        proc.wait()
        output = proc.stdout.read() if proc.stdout else ""
        logger.error(
            'Executing "cmk -d %s" failed with RC:%s! Output:\n%s',
            hostname,
            proc.returncode,
            output,
        )
        raise e


def controller_status_json(controller_path: Path) -> Mapping[str, Any]:
    return json.loads(run([controller_path.as_posix(), "status", "--json"], sudo=True).stdout)


def controller_connection_json(
    controller_status: Mapping[str, Any], site: Site
) -> Mapping[str, Any] | None:
    return next(
        (
            _
            for _ in controller_status["connections"]
            if _["site_id"] == f"{site.http_address}/{site.id}"
        ),
        None,
    )


def wait_until_host_has_services(
    site: Site,
    hostname: HostName,
    *,
    n_services_min: int = 5,
    timeout: int = 120,
    interval: int = 20,
) -> None:
    wait_until(
        lambda: _query_hosts_service_count(site, hostname) > n_services_min,
        timeout=timeout,
        interval=interval,
    )


def _query_hosts_service_count(site: Site, hostname: HostName) -> int:
    return (
        len(services_response.json()["value"])
        # the host might not yet exist at the point where we start waiting
        if (
            services_response := site.openapi.get(f"objects/host/{hostname}/collections/services")
        ).ok
        else 0
    )


def wait_for_baking_job(central_site: Site, expected_start_time: float) -> None:
    waiting_time = 1
    waiting_cycles = 20
    for _ in range(waiting_cycles):
        time.sleep(waiting_time)
        baking_status = central_site.openapi.get_baking_status()
        assert baking_status.state in (
            "initialized",
            "running",
            "finished",
        ), f"Unexpected baking state: {baking_status}"
        assert (
            baking_status.started >= expected_start_time
        ), f"No baking job started after expected starting time: {expected_start_time}"
        if baking_status.state == "finished":
            return
    raise AssertionError(
        f"Now waiting {waiting_cycles * waiting_time} seconds for baking job to finish, giving up..."
    )


def _remove_omd_status_cache() -> None:
    logger.info("Removing omd status agent cache...")
    with execute(
        ["rm", "-f", str(OMD_STATUS_CACHE)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        sudo=True,
    ) as p:
        rc = p.wait()
        p_out, p_err = p.communicate()
        assert rc == 0, f"Failed to remove agent cache.\nSTDOUT: {p_out}\nSTDERR: {p_err}"


def _all_omd_services_running_from_cache(site: Site) -> tuple[bool, str]:
    stdout = site.read_file(OMD_STATUS_CACHE)
    assert f"[{site.id}]" in stdout
    assert "OVERALL" in stdout

    # extract text between '[<site.id>]' and 'OVERALL'
    match_extraction = re.findall(rf"\[{site.id}\]([^\\]*?)OVERALL", stdout)
    sub_stdout = match_extraction[0] if match_extraction else ""

    # find all occurrences of one or more digits in the extracted stdout
    match_assertion = re.findall(r"\d+", sub_stdout)
    return all(int(match) == 0 for match in match_assertion), stdout


def wait_for_agent_cache_omd_status(site: Site, max_count: int = 20, waiting_time: int = 5) -> None:
    """Force re-generation of the omd status agent cache until it matches the current omd status."""
    count = 0

    while site.is_running() and count < max_count:
        if OMD_STATUS_CACHE.exists():
            fully_running, cache_content = _all_omd_services_running_from_cache(site)
            if fully_running:
                logger.info("Agent cache reports site to be fully running")
                return
            logger.info(
                "Agent cache reports site NOT to be fully running. Agent cache content:\n%s",
                cache_content,
            )
            # to force agent cache regeneration we remove the cache file
            _remove_omd_status_cache()

        logger.info("Waiting for agent cache to be generated...")
        time.sleep(waiting_time)
        count += 1

    logger.info("Agent cache not matching the current OMD status")
