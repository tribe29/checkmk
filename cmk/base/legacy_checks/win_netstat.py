#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


from cmk.base.check_legacy_includes.netstat import check_netstat_generic

from cmk.agent_based.legacy.v0_unstable import LegacyCheckDefinition

check_info = {}

# Example output from agent (German Windows XP)
# <<<win_netstat>>>
#
# Aktive Verbindungen
#
#   Proto  Lokale Adresse         Remoteadresse          Status
#   TCP    0.0.0.0:135            0.0.0.0:0              ABHREN
#   TCP    0.0.0.0:445            0.0.0.0:0              ABHREN
#   TCP    0.0.0.0:2869           0.0.0.0:0              ABHREN
#   TCP    0.0.0.0:6556           0.0.0.0:0              ABHREN
#   TCP    10.1.1.99:139          0.0.0.0:0              ABHREN
#   TCP    10.1.1.99:445          10.1.1.123:52820       HERGESTELLT
#   TCP    10.1.1.99:6556         10.1.1.50:43257        WARTEND
#   TCP    10.1.1.99:6556         10.1.1.50:43288        WARTEND
#   TCP    10.1.1.99:6556         10.1.1.50:43309        WARTEND
#   TCP    127.0.0.1:1029         127.0.0.1:5354         HERGESTELLT
#   TCP    127.0.0.1:1030         0.0.0.0:0              ABHREN
#   TCP    127.0.0.1:1040         127.0.0.1:27015        HERGESTELLT
#   TCP    127.0.0.1:5354         0.0.0.0:0              ABHREN
#   TCP    127.0.0.1:5354         127.0.0.1:1029         HERGESTELLT
#   TCP    127.0.0.1:27015        0.0.0.0:0              ABHREN
#   TCP    127.0.0.1:27015        127.0.0.1:1040         HERGESTELLT
#   UDP    0.0.0.0:445            *:*
#   UDP    0.0.0.0:500            *:*
#   UDP    127.0.0.1:1042         *:*
#   UDP    127.0.0.1:1900         *:*

win_netstat_states = {
    # German
    "ABH\x99REN": "LISTENING",
    "HERGESTELLT": "ESTABLISHED",
    "WARTEND": "TIME_WAIT",
    "SCHLIESSEN_WARTEN": "CLOSE_WAIT",
    # Add further states in any required language here. Sorry, Windows
    # has no "unset LANG" ;-)
}


def parse_win_netstat(string_table):
    connections = []
    for line in string_table:
        if line[0] == "TCP":
            proto, local, remote, connstate = line
        elif line[0] == "UDP":
            proto, local, remote = line
            connstate = "LISTEN"
        else:
            continue
        connections.append(
            (
                proto,
                local.rsplit(":", 1),
                remote.rsplit(":", 1),
                win_netstat_states.get(connstate, connstate),
            )
        )
    return connections


check_info["win_netstat"] = LegacyCheckDefinition(
    name="win_netstat",
    parse_function=parse_win_netstat,
    service_name="TCP Connection %s",
    check_function=check_netstat_generic,
    check_ruleset_name="tcp_connections",
)
