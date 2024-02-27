#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from collections.abc import Mapping, Sequence

import pytest

from cmk.plugins.collection.server_side_calls.icmp import active_check_icmp
from cmk.server_side_calls.v1 import (
    ActiveCheckCommand,
    HostConfig,
    IPAddressFamily,
    NetworkAddressConfig,
)

HOST_CONFIG = HostConfig(
    name="hostname",
    resolved_address="0.0.0.1",
    alias="host_alias",
    address_config=NetworkAddressConfig(
        ip_family=IPAddressFamily.IPV4,
        ipv4_address="0.0.0.2",
        ipv6_address="fe80::240",
        additional_ipv4_addresses=["0.0.0.4", "0.0.0.5"],
        additional_ipv6_addresses=[
            "fe80::241",
            "fe80::242",
            "fe80::243",
        ],
    ),
)


@pytest.mark.parametrize(
    "params, expected_result",
    [
        pytest.param(
            {"timeout": 30},
            [
                ActiveCheckCommand(
                    service_description="PING",
                    command_arguments=[
                        "-t",
                        "30",
                        "-w",
                        "200.00,80%",
                        "-c",
                        "500.00,100%",
                        "0.0.0.1",
                    ],
                )
            ],
            id="timeout",
        ),
        pytest.param(
            {"address": "alias"},
            [
                ActiveCheckCommand(
                    service_description="PING",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "host_alias"],
                )
            ],
            id="alias",
        ),
        pytest.param(
            {"address": ("indexed_ipv4address", "1")},
            [
                ActiveCheckCommand(
                    service_description="PING IPv4/1",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "0.0.0.4"],
                )
            ],
            id="indexed ipv4 address",
        ),
        pytest.param(
            {"address": ("indexed_ipv6address", "3")},
            [
                ActiveCheckCommand(
                    service_description="PING IPv6/3",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "-6", "fe80::243"],
                )
            ],
            id="indexed ipv6 address",
        ),
        pytest.param(
            {"address": "all_ipv4addresses"},
            [
                ActiveCheckCommand(
                    service_description="PING all IPv4 Addresses",
                    command_arguments=[
                        "-w",
                        "200.00,80%",
                        "-c",
                        "500.00,100%",
                        "0.0.0.2",
                        "0.0.0.4",
                        "0.0.0.5",
                    ],
                )
            ],
            id="all ipv4 addresses",
        ),
        pytest.param(
            {"address": "all_ipv6addresses"},
            [
                ActiveCheckCommand(
                    service_description="PING all IPv6 Addresses",
                    command_arguments=[
                        "-w",
                        "200.00,80%",
                        "-c",
                        "500.00,100%",
                        "-6",
                        "fe80::240",
                        "fe80::241",
                        "fe80::242",
                        "fe80::243",
                    ],
                )
            ],
            id="all ipv4 addresses",
        ),
        pytest.param(
            {"address": "additional_ipv4addresses"},
            [
                ActiveCheckCommand(
                    service_description="PING",
                    command_arguments=[
                        "-w",
                        "200.00,80%",
                        "-c",
                        "500.00,100%",
                        "0.0.0.4",
                        "0.0.0.5",
                    ],
                )
            ],
            id="additional ipv4 addresses",
        ),
        pytest.param(
            {"address": "additional_ipv6addresses"},
            [
                ActiveCheckCommand(
                    service_description="PING",
                    command_arguments=[
                        "-w",
                        "200.00,80%",
                        "-c",
                        "500.00,100%",
                        "-6",
                        "fe80::241",
                        "fe80::242",
                        "fe80::243",
                    ],
                )
            ],
            id="additional ipv6 addresses",
        ),
        pytest.param(
            {"address": ("explicit", "my.custom.address")},
            [
                ActiveCheckCommand(
                    service_description="PING",
                    command_arguments=[
                        "-w",
                        "200.00,80%",
                        "-c",
                        "500.00,100%",
                        "my.custom.address",
                    ],
                )
            ],
            id="explicit address",
        ),
        pytest.param(
            {"timeout": 30, "multiple_services": True},
            [
                ActiveCheckCommand(
                    service_description="PING 0.0.0.1",
                    command_arguments=[
                        "-t",
                        "30",
                        "-w",
                        "200.00,80%",
                        "-c",
                        "500.00,100%",
                        "0.0.0.1",
                    ],
                )
            ],
            id="timeout multiple services",
        ),
        pytest.param(
            {"address": "alias", "multiple_services": True},
            [
                ActiveCheckCommand(
                    service_description="PING host_alias",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "host_alias"],
                )
            ],
            id="alias multiple services",
        ),
        pytest.param(
            {"address": ("indexed_ipv4address", "1"), "multiple_services": True},
            [
                ActiveCheckCommand(
                    service_description="PING 0.0.0.4",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "0.0.0.4"],
                )
            ],
            id="indexed ipv4 address multiple services",
        ),
        pytest.param(
            {"address": ("indexed_ipv6address", "3"), "multiple_services": True},
            [
                ActiveCheckCommand(
                    service_description="PING fe80::243",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "-6", "fe80::243"],
                )
            ],
            id="indexed ipv6 address multiple services",
        ),
        pytest.param(
            {"address": "all_ipv4addresses", "multiple_services": True},
            [
                ActiveCheckCommand(
                    service_description="PING 0.0.0.2",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "0.0.0.2"],
                ),
                ActiveCheckCommand(
                    service_description="PING 0.0.0.4",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "0.0.0.4"],
                ),
                ActiveCheckCommand(
                    service_description="PING 0.0.0.5",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "0.0.0.5"],
                ),
            ],
            id="all ipv4 addresses multiple services",
        ),
        pytest.param(
            {"address": "all_ipv6addresses", "multiple_services": True},
            [
                ActiveCheckCommand(
                    service_description="PING fe80::240",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "-6", "fe80::240"],
                ),
                ActiveCheckCommand(
                    service_description="PING fe80::241",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "-6", "fe80::241"],
                ),
                ActiveCheckCommand(
                    service_description="PING fe80::242",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "-6", "fe80::242"],
                ),
                ActiveCheckCommand(
                    service_description="PING fe80::243",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "-6", "fe80::243"],
                ),
            ],
            id="all ipv4 addresses multiple services",
        ),
        pytest.param(
            {"address": "additional_ipv4addresses", "multiple_services": True},
            [
                ActiveCheckCommand(
                    service_description="PING 0.0.0.4",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "0.0.0.4"],
                ),
                ActiveCheckCommand(
                    service_description="PING 0.0.0.5",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "0.0.0.5"],
                ),
            ],
            id="additional ipv4 addresses multiple services",
        ),
        pytest.param(
            {"address": "additional_ipv6addresses", "multiple_services": True},
            [
                ActiveCheckCommand(
                    service_description="PING fe80::241",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "-6", "fe80::241"],
                ),
                ActiveCheckCommand(
                    service_description="PING fe80::242",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "-6", "fe80::242"],
                ),
                ActiveCheckCommand(
                    service_description="PING fe80::243",
                    command_arguments=["-w", "200.00,80%", "-c", "500.00,100%", "-6", "fe80::243"],
                ),
            ],
            id="additional ipv6 addresses multiple services",
        ),
        pytest.param(
            {"address": ("explicit", "my.custom.address"), "multiple_services": True},
            [
                ActiveCheckCommand(
                    service_description="PING my.custom.address",
                    command_arguments=[
                        "-w",
                        "200.00,80%",
                        "-c",
                        "500.00,100%",
                        "my.custom.address",
                    ],
                )
            ],
            id="explicit address multiple services",
        ),
    ],
)
def test_generate_icmp_services(
    params: Mapping[str, object],
    expected_result: Sequence[ActiveCheckCommand],
) -> None:
    services = list(
        active_check_icmp.commands_function(
            active_check_icmp.parameter_parser(params),
            HOST_CONFIG,
            {},
        )
    )
    assert services == expected_result
