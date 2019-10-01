#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    Percentage,
    Tuple,
    Transform,
)

from cmk.gui.plugins.wato import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersOperatingSystem,
)


def _parameter_valuespec_threads():
    return Transform(
        Dictionary(elements=[
            ("levels",
             Tuple(
                 title=_("Absolute levels"),
                 elements=[
                     Integer(title=_("Warning at"), unit=_("threads"), default_value=2000),
                     Integer(title=_("Critical at"), unit=_("threads"), default_value=4000)
                 ],
             )),
            ("levels_percent",
             Tuple(
                 title=_("Relative levels"),
                 elements=[
                     Percentage(title=_("Warning at"), default_value=80),
                     Percentage(title=_("Critical at"), default_value=90)
                 ],
             )),
        ],),
        forth=lambda params: params if isinstance(params, dict) else {'levels': params},
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name="threads",
        group=RulespecGroupCheckParametersOperatingSystem,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_threads,
        title=lambda: _("Number of threads"),
    ))
