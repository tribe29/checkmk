#!/usr/bin/env python3
# Copyright (C) 2021 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import logging
import shutil
from pathlib import Path
from typing import Iterator

import pytest

import cmk.utils.paths
from cmk.utils.hostaddress import HostAddress, HostName
from cmk.utils.site import omd_site
from cmk.utils.user import UserId

from cmk.gui.watolib.hosts_and_folders import Folder, folder_tree

from cmk.update_config.plugins.actions.migrate_parents_mk import MigrateParentsMK

EXAMPLE_PARENTS_EMPTY = """# Automatically created by --scan-parents at Mon Apr 15 07:52:26 2024

# Do not edit this file. If you want to convert an
# artificial gateway host into a permanent one, then
# move its definition into another *.mk file
# Parents which are not listed in your all_hosts:
all_hosts += []

# IP addresses of parents not listed in all_hosts:
ipaddresses.update({})

# Parent definitions
parents += []
"""

EXAMPLE_CHECKMK_PARENTS = """# Automatically created by --scan-parents at Mon Apr 15 07:52:26 2024

# Do not edit this file. If you want to convert an
# artificial gateway host into a permanent one, then
# move its definition into another *.mk file
# Parents which are not listed in your all_hosts:
all_hosts += ['fra1.cc.as48314.net|parent|ping']

# IP addresses of parents not listed in all_hosts:
ipaddresses.update({'fra1.cc.as48314.net': '194.45.196.22'})

# Parent definitions
parents += [('fra1.cc.as48314.net', ['checkmk.com'])]
"""

EXAMPLE_NESTED_PARENTS_WITH_MISSING_HOST = """# Automatically created by --scan-parents at Mon Apr 15 07:52:26 2024

# Do not edit this file. If you want to convert an
# artificial gateway host into a permanent one, then
# move its definition into another *.mk file
# Parents which are not listed in your all_hosts:
all_hosts += ['fra1.cc.as48314.net|parent|ping', 'fra2.cc.as48314.net|parent|ping']

# IP addresses of parents not listed in all_hosts:
ipaddresses.update({'fra1.cc.as48314.net': '194.45.196.22', 'fra2.cc.as48314.net': '194.45.196.23'})

# Parent definitions
parents += [('fra1.cc.as48314.net', ['checkmk.com']), ('fra2.cc.as48314.net', ['fra1.cc.as48314.net'])]
"""


@pytest.fixture(name="conf_root")
def _conf_root(with_admin_login: UserId, load_config: None) -> Iterator[Folder]:
    # Ensure we have clean folder/host caches
    tree = folder_tree()
    tree.invalidate_caches()
    root = tree.root_folder()
    Path(cmk.utils.paths.main_config_file).touch()

    yield root

    # Cleanup WATO folders created by the test
    root_path = Path(root.filesystem_path())
    shutil.rmtree(root_path, ignore_errors=True)
    root_path.mkdir(parents=True, exist_ok=True)


def run_migrate() -> None:
    return MigrateParentsMK(
        name="migrate_parent_scan_config", title="Migrate CLI parent scan config", sort_index=40
    )(logging.getLogger())


def test_parents_created(conf_root: Folder) -> None:
    confd_path = Path(conf_root.filesystem_path()).parents[0]
    (confd_path / "some_parents.mk").write_text(EXAMPLE_CHECKMK_PARENTS)

    hostname = HostName("checkmk.com")
    local_site_id = omd_site()
    conf_subfolder = conf_root.create_subfolder("some_subfolder", "Some Subfolder", {})
    conf_subfolder.create_hosts([(hostname, {"site": local_site_id}, None)])
    assert conf_subfolder.host(hostname) is not None, "Test setup failed, host not created"

    run_migrate()

    root = folder_tree().root_folder()
    assert (subfolder := root.subfolder("some_subfolder"))
    assert (host := subfolder.host(hostname))
    assert (parent_folder := root.subfolder("migrated_parents"))
    assert (parent_host := parent_folder.host(HostName("fra1.cc.as48314.net")))
    parent_attributes = parent_host.effective_attributes()
    assert parent_attributes["ipaddress"] == HostAddress("194.45.196.22")
    assert parent_attributes["tag_agent"] == "no-agent"
    assert parent_attributes["tag_snmp_ds"] == "no-snmp"
    assert host.parents() == [parent_host.id()]
    assert parent_host.site_id() == local_site_id
    assert not (confd_path / "some_parents.mk").exists()
    assert (confd_path / "some_parents.mk_inactive").exists()


def test_nested_parents_still_created_if_host_is_missing(conf_root: Folder) -> None:
    confd_path = Path(conf_root.filesystem_path()).parents[0]
    (confd_path / "some_parents.mk").write_text(EXAMPLE_NESTED_PARENTS_WITH_MISSING_HOST)

    run_migrate()

    root = folder_tree().root_folder()
    assert (parent_folder := root.subfolder("migrated_parents"))
    assert (parent_host := parent_folder.host(HostName("fra1.cc.as48314.net")))
    assert parent_host.effective_attributes()["ipaddress"] == HostAddress("194.45.196.22")
    assert (grandparent_host := parent_folder.host(HostName("fra2.cc.as48314.net")))
    assert grandparent_host.effective_attributes()["ipaddress"] == HostAddress("194.45.196.23")
    assert parent_host.parents() == [grandparent_host.id()]
    assert parent_host.site_id() == omd_site()
    assert parent_host.site_id() == grandparent_host.site_id()
    assert not (confd_path / "some_parents.mk").exists()
    assert (confd_path / "some_parents.mk_inactive").exists()


def test_no_new_parents_on_empty_parents_mk(conf_root: Folder) -> None:
    confd_path = Path(conf_root.filesystem_path()).parents[0]
    (confd_path / "some_parents.mk").write_text(EXAMPLE_PARENTS_EMPTY)

    run_migrate()

    root = folder_tree().root_folder()
    assert root.subfolder("migrated_parents") is None
    assert not (confd_path / "some_parents.mk").exists()
    assert (confd_path / "some_parents.mk_inactive").exists()
