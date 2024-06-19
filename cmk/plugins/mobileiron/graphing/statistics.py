#!/usr/bin/env python3
# Copyright (C) 2024 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.graphing.v1 import graphs, metrics, perfometers, Title

UNIT_TIME = metrics.Unit(metrics.TimeNotation())
UNIT_COUNTER = metrics.Unit(metrics.DecimalNotation(""), metrics.StrictPrecision(2))
UNIT_PERCENTAGE = metrics.Unit(metrics.DecimalNotation("%"))

metric_mobileiron_devices_total = metrics.Metric(
    name="mobileiron_devices_total",
    title=Title("Total devices"),
    unit=UNIT_COUNTER,
    color=metrics.Color.BLACK,
)
metric_mobileiron_non_compliant = metrics.Metric(
    name="mobileiron_non_compliant",
    title=Title("Non-compliant devices"),
    unit=UNIT_COUNTER,
    color=metrics.Color.BLUE,
)
metric_mobileiron_non_compliant_summary = metrics.Metric(
    name="mobileiron_non_compliant_summary",
    title=Title("Non-compliant devices"),
    unit=UNIT_PERCENTAGE,
    color=metrics.Color.LIGHT_BLUE,
)

perfometer_mobileiron_non_compliant_summary = perfometers.Perfometer(
    name="mobileiron_non_compliant_summary",
    focus_range=perfometers.FocusRange(
        perfometers.Closed(0),
        perfometers.Closed(100.0),
    ),
    segments=["mobileiron_non_compliant_summary"],
)

graph_mobileiron_compliances = graphs.Graph(
    name="mobileiron_compliances",
    title=Title("Total non-compliant devices"),
    compound_lines=["mobileiron_non_compliant"],
    simple_lines=["mobileiron_devices_total"],
)
