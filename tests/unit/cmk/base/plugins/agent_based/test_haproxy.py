#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import mock
import pytest
from time import time

from cmk.base.plugins.agent_based.agent_based_api.v1 import Result, State, Metric, Service
from cmk.base.plugins.agent_based.haproxy import (parse_haproxy, discover_haproxy_frontend,
                                                  discover_haproxy_server, check_haproxy_frontend,
                                                  check_haproxy_server, Section)


@pytest.mark.parametrize("info, expected_parsed", [((
    [[
        "https_t3test.tgic.de", "FRONTEND", "", "", "0", "0", "2000", "invalid value", "0", "0",
        "0", "0", "0", "", "", "", "", "UP", "", "", "", "", "", "", "", "", "1", "2", "0", "", "",
        "", "0", "0", "0", "0", "", "", "", "0", "0", "0", "0", "0", "0", "", "0", "0", "0", "", "",
        "0", "0", "0", "0", "", "", "", "", "", "", "", ""
    ]],
    Section(frontends={}, servers={}),
))])
def test_parse_haproxy(info, expected_parsed):
    data = parse_haproxy(info)
    assert data == expected_parsed


@pytest.mark.parametrize("info, expected_result", [(
    [[
        "https_t3test.tgic.de", "FRONTEND", "", "", "0", "0", "2000", "0", "0", "0", "0", "0", "0",
        "", "", "", "", "UP", "", "", "", "", "", "", "", "", "1", "2", "0", "", "", "", "0", "0",
        "0", "0", "", "", "", "0", "0", "0", "0", "0", "0", "", "0", "0", "0", "", ""
    ],
     [
         "t3test", "t3test", "0", "0", "0", "0", "", "0", "0", "0", "", "0", "", "0", "0", "0", "0",
         "UP", "1", "1", "0", "0", "0", "363417", "0", "", "1", "3", "1", "", "0", "", "2", "0", "",
         "0", "L4OK", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "0", "0", "", "", "",
         "", "-1", "", "", "0", "0", "0", "0", ""
     ]],
    [Service(item="https_t3test.tgic.de")],
)])
def test_discover_haproxy_frontent(info, expected_result):
    data = parse_haproxy(info)
    result = discover_haproxy_frontend(data)
    assert list(result) == expected_result


@pytest.mark.parametrize("item, params, info, expected_result", [
    (
        "https_t3test.tgic.de",
        {
            "OPEN": 0
        },
        [[
            "# pxname", "svname", "qcur", "qmax", "scur", "smax", "slim", "stot", "bin", "bout",
            "dreq", "dresp", "ereq", "econ", "eresp", "wretr", "wredis", "status", "weight", "act",
            "bck", "chkfail", "chkdown", "lastchg", "downtime", "qlimit", "pid", "iid", "sid",
            "throttle", "lbtot", "tracked", "type", "rate", "rate_lim", "rate_max", "check_status",
            "check_code", "check_duration", "hrsp_1xx", "hrsp_2xx", "hrsp_3xx", "hrsp_4xx",
            "hrsp_5xx", "hrsp_other", "hanafail", "req_rate", "req_rate_max", "req_tot", "cli_abrt",
            "srv_abrt", "comp_in", "comp_out", "comp_byp", "comp_rsp", "lastsess", "last_chk",
            "last_agt", "qtime", "ctime", "rtime", "ttime", ""
        ],
         [
             "https_t3test.tgic.de", "FRONTEND", "", "", "0", "0", "2000", "0", "0", "0", "0", "0",
             "0", "", "", "", "", "OPEN", "", "", "", "", "", "", "", "", "1", "2", "0",
             "", "", "", "0", "0", "0", "0", "", "", "", "0", "0", "0", "0", "0", "0", "", "0", "0",
             "0", "", "", "0", "0", "0", "0", "", "", "", "", "", "", "", ""
         ]],
        [
            Result(state=State.OK, summary="Status: OPEN"),
            Result(state=State.OK, summary="Session Rate: 0.00"),
            Metric("session_rate", 0.0)
        ],
    ),
    (
        "https_t3test.tgic.de",
        {
            "STOP": 1
        },
        [[
            "https_t3test.tgic.de", "FRONTEND", "", "", "0", "0", "2000", "0", "0", "0", "0", "0",
            "0", "", "", "", "", "STOP", "", "", "", "", "", "", "", "", "1", "2", "0", "", "", "",
            "0", "0", "0", "0", "", "", "", "0", "0", "0", "0", "0", "0", "", "0", "0", "0", "", "",
            "0", "0", "0", "0", "", "", "", "", "", "", "", ""
        ]],
        [
            Result(state=State.WARN, summary="Status: STOP"),
            Result(state=State.OK, summary="Session Rate: 0.00"),
            Metric('session_rate', 0.0)
        ],
    ),
    (
        "t3test/t3test",
        {},
        [[
            "https_t3test.tgic.de", "FRONTEND", "", "", "0", "0", "2000", "0", "0", "0", "0", "0",
            "0", "", "", "", "", "STOP", "", "", "", "", "", "", "", "", "1", "2", "0", "", "", "",
            "0", "0", "0", "0", "", "", "", "0", "0", "0", "0", "0", "0", "", "0", "0", "0", "", "",
            "0", "0", "0", "0", "", "", "", "", "", "", "", ""
        ]],
        [],
    )
])
@mock.patch("cmk.base.plugins.agent_based.haproxy.get_value_store",
            mock.MagicMock(return_value={"sessions.https_t3test.tgic.de": (time(), 0.0)}))
def test_haproxy_frontend(item, params, info, expected_result):
    data = parse_haproxy(info)
    result = check_haproxy_frontend(item, params, data)
    assert list(result) == expected_result


@pytest.mark.parametrize("info, expected_result", [(
    [[
        "https_t3test.tgic.de", "FRONTEND", "", "", "0", "0", "2000", "invalid value", "0", "0",
        "0", "0", "0", "", "", "", "", "UP", "", "", "", "", "", "", "", "", "1", "2", "0", "", "",
        "", "0", "0", "0", "0", "", "", "", "0", "0", "0", "0", "0", "0", "", "0", "0", "0", "", ""
    ],
     [
         "t3test", "t3test", "0", "0", "0", "0", "", "0", "0", "0", "", "0", "", "0", "0", "0", "0",
         "UP", "1", "1", "0", "0", "0", "363417", "0", "", "1", "3", "1", "", "0", "", "2", "0", "",
         "0", "L4OK", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "0", "0", "", "", "",
         "", "-1", "", "", "0", "0", "0", "0", ""
     ]],
    [Service(item="t3test/t3test")],
)])
def test_discover_haproxy_server(info, expected_result):
    data = parse_haproxy(info)
    result = discover_haproxy_server(data)
    assert list(result) == expected_result


@pytest.mark.parametrize("item, params, info, expected_result", [
    (
        "t3test/t3test",
        {
            "UP": 0
        },
        [[
            "t3test", "t3test", "0", "0", "0", "0", "", "0", "0", "0", "", "0", "", "0", "0", "0",
            "0", "UP", "1", "1", "0", "0", "0", "363417", "0", "", "1", "3", "1", "", "0", "", "2",
            "0", "", "0", "L4OK", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "0", "0",
            "", "", "", "", "-1", "", "", "0", "0", "0", "0", ""
        ]],
        [
            Result(state=State.OK, summary="Status: UP"),
            Result(state=State.OK, summary="Active"),
            Result(state=State.OK, summary="Layer Check: L4OK"),
            Result(state=State.OK, summary="Up since 4 days 4 hours")
        ],
    ),
    (
        "t3test/t3test",
        {
            "UP": 1
        },
        [[
            "t3test", "t3test", "0", "0", "0", "0", "", "0", "0", "0", "", "0", "", "0", "0", "0",
            "0", "UP", "1", "0", "1", "0", "0", "363417", "0", "", "1", "3", "1", "", "0", "", "2",
            "0", "", "0", "L4OK", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "0", "0",
            "", "", "", "", "-1", "", "", "0", "0", "0", "0", ""
        ]],
        [
            Result(state=State.WARN, summary="Status: UP"),
            Result(state=State.OK, summary="Backup"),
            Result(state=State.OK, summary="Layer Check: L4OK"),
            Result(state=State.OK, summary="Up since 4 days 4 hours")
        ],
    ),
    (
        "t3test/t3test",
        {
            "UP": 0
        },
        [[
            "t3test", "t3test", "0", "0", "0", "0", "", "0", "0", "0", "", "0", "", "0", "0", "0",
            "0", "UP", "1", "0", "0", "0", "0", "363417", "0", "", "1", "3", "1", "", "0", "", "2",
            "0", "", "0", "L4OK", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "0", "0",
            "", "", "", "", "-1", "", "", "0", "0", "0", "0", ""
        ]],
        [
            Result(state=State.OK, summary="Status: UP"),
            Result(state=State.CRIT, summary="Neither active nor backup"),
            Result(state=State.OK, summary="Layer Check: L4OK"),
            Result(state=State.OK, summary="Up since 4 days 4 hours")
        ],
    ),
    (
        "t3test/t3test",
        {
            "UP": 0
        },
        [[
            "t3test", "t3test", "0", "0", "0", "0", "", "0", "0", "0", "", "0", "", "0", "0", "0",
            "0", "UP", "1", "1", "0", "0", "0", "None", "0", "", "1", "3", "1", "", "0", "", "2",
            "0", "", "0", "L4OK", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "0", "0",
            "", "", "", "", "-1", "", "", "0", "0", "0", "0", ""
        ]],
        [
            Result(state=State.OK, summary="Status: UP"),
            Result(state=State.OK, summary="Active"),
            Result(state=State.OK, summary="Layer Check: L4OK")
        ],
    ),
    (
        "t3test/t3test",
        {
            "MAINT": 3
        },
        [[
            "t3test", "t3test", "0", "0", "0", "0", "", "0", "0", "0", "", "0", "", "0", "0", "0",
            "0", "MAINT", "1", "1", "0", "0", "0", "363417", "0", "", "1", "3", "1", "", "0", "",
            "2", "0", "", "0", "L4OK", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "0",
            "0", "", "", "", "", "-1", "", "", "0", "0", "0", "0", ""
        ]],
        [
            Result(state=State.UNKNOWN, summary="Status: MAINT"),
            Result(state=State.OK, summary="Active"),
            Result(state=State.OK, summary="Layer Check: L4OK"),
            Result(state=State.OK, summary="Up since 4 days 4 hours")
        ],
    ),
    (
        "https_t3test.tgic.de",
        {},
        [[
            "t3test", "t3test", "0", "0", "0", "0", "", "0", "0", "0", "", "0", "", "0", "0", "0",
            "0", "MAINT", "1", "1", "0", "0", "0", "363417", "0", "", "1", "3", "1", "", "0", "",
            "2", "0", "", "0", "L4OK", "", "0", "0", "0", "0", "0", "0", "0", "0", "", "", "", "0",
            "0", "", "", "", "", "-1", "", "", "0", "0", "0", "0", ""
        ]],
        [],
    )
])
def test_haproxy_server(item, params, info, expected_result):
    data = parse_haproxy(info)
    result = check_haproxy_server(item, params, data)
    assert list(result) == expected_result
