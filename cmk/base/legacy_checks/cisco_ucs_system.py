#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.


from cmk.base.check_api import LegacyCheckDefinition
from cmk.base.check_legacy_includes.cisco_ucs import DETECT, map_operability
from cmk.base.config import check_info
from cmk.base.plugins.agent_based.agent_based_api.v1 import SNMPTree

# comNET GmbH, Fabian Binder - 2018-05-07

# .1.3.6.1.4.1.9.9.719.1.9.35.1.32 cucsComputeRackUnitModel
# .1.3.6.1.4.1.9.9.719.1.9.35.1.47 cucsComputeRackUnitSerial
# .1.3.6.1.4.1.9.9.719.1.9.35.1.43 cucsComputeRackUnitOperability


def inventory_cisco_ucs_system(info):
    return [(None, None)]


def check_cisco_ucs_system(_no_item, _no_params, info):
    model, serial, status = info[0]
    state, state_readable = map_operability.get(status, (3, "Unknown, status code %s" % status))
    return state, f"Status: {state_readable}, Model: {model}, SN: {serial}"


check_info["cisco_ucs_system"] = LegacyCheckDefinition(
    detect=DETECT,
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.9.9.719.1.9.35.1",
        oids=["32", "47", "43"],
    ),
    service_name="System health",
    discovery_function=inventory_cisco_ucs_system,
    check_function=check_cisco_ucs_system,
)
