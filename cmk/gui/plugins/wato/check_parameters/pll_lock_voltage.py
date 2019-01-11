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
    DropdownChoice,
    Float,
    ListOf,
    Tuple,
)
from cmk.gui.plugins.wato import (
    RulespecGroupCheckParametersEnvironment,
    register_check_parameters,
)

register_check_parameters(
    RulespecGroupCheckParametersEnvironment,
    "pll_lock_voltage",
    _("Lock Voltage for PLLs"),
    Dictionary(
        help=_("PLL lock voltages by freqency"),
        elements=[
            ("rx",
             ListOf(
                 Tuple(
                     elements=[
                         Float(title=_("Frequencies up to"), unit=u"MHz"),
                         Float(title=_("Warning below"), unit=u"V"),
                         Float(title=_("Critical below"), unit=u"V"),
                         Float(title=_("Warning at or above"), unit=u"V"),
                         Float(title=_("Critical at or above"), unit=u"V"),
                     ],),
                 title=_("Lock voltages for RX PLL"),
                 help=_("Specify frequency ranges by the upper boundary of the range "
                        "to which the voltage levels are to apply. The list is sorted "
                        "automatically when saving."),
                 movable=False)),
            ("tx",
             ListOf(
                 Tuple(
                     elements=[
                         Float(title=_("Frequencies up to"), unit=u"MHz"),
                         Float(title=_("Warning below"), unit=u"V"),
                         Float(title=_("Critical below"), unit=u"V"),
                         Float(title=_("Warning at or above"), unit=u"V"),
                         Float(title=_("Critical at or above"), unit=u"V"),
                     ],),
                 title=_("Lock voltages for TX PLL"),
                 help=_("Specify frequency ranges by the upper boundary of the range "
                        "to which the voltage levels are to apply. The list is sorted "
                        "automatically when saving."),
                 movable=False)),
        ],
        optional_keys=["rx", "tx"],
    ),
    DropdownChoice(title=_("RX/TX"), choices=[("RX", _("RX")), ("TX", _("TX"))]),
    match_type="dict",
)
