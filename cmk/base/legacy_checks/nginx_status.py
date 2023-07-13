#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# Example output:
# <<<nginx_status>>>
# 127.0.0.1 80 Active connections: 1
# 127.0.0.1 80 server accepts handled requests
# 127.0.0.1 80  12 12 12
# 127.0.0.1 80 Reading: 0 Writing: 1 Waiting: 0


import time

from cmk.base.check_api import check_levels, get_rate, LegacyCheckDefinition
from cmk.base.config import check_info


def parse_nginx_status(info):
    if len(info) % 4 != 0:
        # Every instance block consists of four lines
        # Multiple block may occur.
        return {}

    data = {}
    for i, line in enumerate(info):
        address, port = line[:2]
        if len(line) < 3:
            continue  # Skip unexpected lines
        item = "%s:%s" % (address, port)

        if item not in data:
            # new server block start
            data[item] = {
                "active": int(info[i + 0][4]),
                "accepted": int(info[i + 2][2]),
                "handled": int(info[i + 2][3]),
                "requests": int(info[i + 2][4]),
                "reading": int(info[i + 3][3]),
                "writing": int(info[i + 3][5]),
                "waiting": int(info[i + 3][7]),
            }

    return data


def check_nginx_status(item, params, parsed):
    if not (data := parsed.get(item)):
        return
    if params is None:
        params = {}

    # Add some more values, derived from the raw ones...
    computed_values = {}
    computed_values["requests_per_conn"] = 1.0 * data["requests"] / data["handled"]

    this_time = int(time.time())
    for key in ["accepted", "handled", "requests"]:
        per_sec = get_rate("nginx_status.%s" % key, this_time, data[key])
        computed_values["%s_per_sec" % key] = per_sec

    state, txt, perf = check_levels(
        data["active"],
        "active",
        params.get("active_connections"),
        infoname="Active",
        human_readable_func=lambda i: "%d" % i,
    )
    txt += " (%d reading, %d writing, %d waiting)" % (
        data["reading"],
        data["writing"],
        data["waiting"],
    )
    yield state, txt, perf
    yield 0, "", [(key, data[key]) for key in ("reading", "writing", "waiting")]

    requests_rate = computed_values["requests_per_sec"]
    state, txt, perf = check_levels(requests_rate, "requests", None, infoname="Requests", unit="/s")
    txt += " (%0.2f/Connection)" % computed_values["requests_per_conn"]
    yield state, txt, perf

    yield 0, "Accepted: %0.2f/s" % computed_values["accepted_per_sec"], [
        ("accepted", data["accepted"])
    ]
    yield 0, "Handled: %0.2f/s" % computed_values["handled_per_sec"], [("handled", data["handled"])]


def discover_nginx_status(section):
    yield from ((item, {}) for item in section)


check_info["nginx_status"] = LegacyCheckDefinition(
    parse_function=parse_nginx_status,
    service_name="Nginx %s Status",
    discovery_function=discover_nginx_status,
    check_function=check_nginx_status,
    check_ruleset_name="nginx_status",
)
