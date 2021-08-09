#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest

from tests.testlib import Check

pytestmark = pytest.mark.checks

_SECTION = {
    "sensor1": {
        "max_abs_float": "38.18",
        "max_day_float": "25.31",
        "min_abs_float": "20.12",
        "min_day_float": "25.06",
        "name": "Gerät Intern",
        "unit": "°C",
        "value_display": "25.18 °C",
        "value_float": "25.18",
        "value_int": "2518",
        "value_string": "25.18",
    },
    "sensor105": {
        "max_abs_float": "70.06",
        "max_day_float": "61.47",
        "min_abs_float": "51.29",
        "min_day_float": "59.93",
        "name": "Feuchtigkeit",
        "unit": "%",
        "value_display": "60.62 %",
        "value_float": "60.62",
        "value_int": "6061",
        "value_string": "60.62",
    },
    "sensor112": {
        "max_abs_float": "20.71",
        "max_day_float": "20.26",
        "min_abs_float": "19.58",
        "min_day_float": "19.56",
        "name": "Serverraum",
        "unit": "°C",
        "value_display": "19.80 °C",
        "value_float": "19.80",
        "value_int": "1979",
        "value_string": "19.80",
    },
    "sensor113": {
        "max_abs_float": "49.54",
        "max_day_float": "46.53",
        "min_abs_float": "44.30",
        "min_day_float": "44.30",
        "name": "Serverraum",
        "unit": "%",
        "value_display": "45.70 %",
        "value_float": "45.70",
        "value_int": "4570",
        "value_string": "45.70",
    },
    "sensor115": {
        "max_abs_float": "23.43",
        "max_day_float": "21.56",
        "min_abs_float": "20.75",
        "min_day_float": "21.18",
        "name": "Schrank 8",
        "unit": "°C",
        "value_display": "21.50 °C",
        "value_float": "21.50",
        "value_int": "2150",
        "value_string": "21.50",
    },
    "sensor130": {
        "max_abs_float": "18.93",
        "max_day_float": "17.00",
        "min_abs_float": "16.37",
        "min_day_float": "16.37",
        "name": "Dachboden",
        "unit": "°C",
        "value_display": "16.56 °C",
        "value_float": "16.56",
        "value_int": "1655",
        "value_string": "16.56",
    },
    "sensor2": {
        "alarm1": "0",
        "function": "2",
        "limit_high": "25.00",
        "limit_low": "5.00",
        "maximum": "0.00",
        "minimum": "100.00",
        "name": "Humidity1",
        "value_float": "10.00",
        "value_int": "10",
        "value_string": "10.00",
    },
    "system": {
        "date": "29.10.2014",
        "devicename": "ALL4500",
        "devicetype": "ALL4500",
        "sys": "66141",
        "time": "08:28:36",
    },
}


def test_parse_allnet_ip_sensoric() -> None:
    assert Check("allnet_ip_sensoric").run_parse([
        ["sensor1.max_abs_float", "38.18"],
        ["sensor1.max_day_float", "25.31"],
        ["sensor1.min_abs_float", "20.12"],
        ["sensor1.min_day_float", "25.06"],
        ["sensor1.name", "Gerät Intern"],
        ["sensor1.unit", "°C"],
        ["sensor1.value_display", "25.18 °C"],
        ["sensor1.value_float", "25.18"],
        ["sensor1.value_int", "2518"],
        ["sensor1.value_string", "25.18"],
        ["sensor2.alarm1", "0"],
        ["sensor2.function", "2"],
        ["sensor2.limit_high", "25.00"],
        ["sensor2.limit_low", "5.00"],
        ["sensor2.maximum", "0.00"],
        ["sensor2.minimum", "100.00"],
        ["sensor2.name", "Humidity1"],
        ["sensor2.value_float", "10.00"],
        ["sensor2.value_int", "10"],
        ["sensor2.value_string", "10.00"],
        ["sensor105.max_abs_float", "70.06"],
        ["sensor105.max_day_float", "61.47"],
        ["sensor105.min_abs_float", "51.29"],
        ["sensor105.min_day_float", "59.93"],
        ["sensor105.name", "Feuchtigkeit"],
        ["sensor105.unit", "%"],
        ["sensor105.value_display", "60.62 %"],
        ["sensor105.value_float", "60.62"],
        ["sensor105.value_int", "6061"],
        ["sensor105.value_string", "60.62"],
        ["sensor112.max_abs_float", "20.71"],
        ["sensor112.max_day_float", "20.26"],
        ["sensor112.min_abs_float", "19.58"],
        ["sensor112.min_day_float", "19.56"],
        ["sensor112.name", "Serverraum"],
        ["sensor112.unit", "°C"],
        ["sensor112.value_display", "19.80 °C"],
        ["sensor112.value_float", "19.80"],
        ["sensor112.value_int", "1979"],
        ["sensor112.value_string", "19.80"],
        ["sensor113.max_abs_float", "49.54"],
        ["sensor113.max_day_float", "46.53"],
        ["sensor113.min_abs_float", "44.30"],
        ["sensor113.min_day_float", "44.30"],
        ["sensor113.name", "Serverraum"],
        ["sensor113.unit", "%"],
        ["sensor113.value_display", "45.70 %"],
        ["sensor113.value_float", "45.70"],
        ["sensor113.value_int", "4570"],
        ["sensor113.value_string", "45.70"],
        ["sensor115.max_abs_float", "23.43"],
        ["sensor115.max_day_float", "21.56"],
        ["sensor115.min_abs_float", "20.75"],
        ["sensor115.min_day_float", "21.18"],
        ["sensor115.name", "Schrank 8"],
        ["sensor115.unit", "°C"],
        ["sensor115.value_display", "21.50 °C"],
        ["sensor115.value_float", "21.50"],
        ["sensor115.value_int", "2150"],
        ["sensor115.value_string", "21.50"],
        ["sensor130.max_abs_float", "18.93"],
        ["sensor130.max_day_float", "17.00"],
        ["sensor130.min_abs_float", "16.37"],
        ["sensor130.min_day_float", "16.37"],
        ["sensor130.name", "Dachboden"],
        ["sensor130.unit", "°C"],
        ["sensor130.value_display", "16.56 °C"],
        ["sensor130.value_float", "16.56"],
        ["sensor130.value_int", "1655"],
        ["sensor130.value_string", "16.56"],
        ["system.date", "29.10.2014"],
        ["system.devicename", "ALL4500"],
        ["system.devicetype", "ALL4500"],
        ["system.sys", "66141"],
        ["system.time", "08:28:36"],
    ]) == _SECTION


def test_inventory_allnet_ip_sensoric_humidity() -> None:
    assert Check("allnet_ip_sensoric.humidity").run_discovery(_SECTION) == [
        ('Feuchtigkeit Sensor 105', 'allnet_ip_sensoric_humidity_default_levels'),
        ('Serverraum Sensor 113', 'allnet_ip_sensoric_humidity_default_levels'),
        ('Humidity1 Sensor 2', 'allnet_ip_sensoric_humidity_default_levels'),
    ]
