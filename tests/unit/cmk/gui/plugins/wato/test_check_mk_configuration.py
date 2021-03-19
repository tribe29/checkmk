#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import os

import pytest  # type: ignore[import]

import cmk.gui.config as config
from cmk.gui.valuespec import (
    DropdownChoice,)

from cmk.gui.plugins.wato.check_mk_configuration import (ConfigVariableGroupUserInterface,
                                                         _transform_automatic_rediscover_parameters)

from cmk.gui.plugins.wato import (
    config_variable_registry,
    ConfigDomainGUI,
)


@pytest.fixture(autouse=True)
def initialize_default_config():
    config._initialize_with_default_config()


def test_ui_theme_registration():
    var = config_variable_registry["ui_theme"]()
    assert var.domain() == ConfigDomainGUI
    assert var.group() == ConfigVariableGroupUserInterface

    valuespec = var.valuespec()
    assert isinstance(valuespec, DropdownChoice)
    assert valuespec.choices() == config.theme_choices()


def test_ui_theme_default_value(register_builtin_html):
    var = config_variable_registry["ui_theme"]()

    default_setting = var.domain()().default_globals()[var.ident()]
    assert default_setting == "modern-dark"

    assert var.valuespec().value_to_text(default_setting) == "Dark"


@pytest.mark.parametrize(
    "parameters, result",
    [
        ({}, {}),
        # These params have to be transformed
        ({
            "other_opt": "other opt",
            "service_whitelist": ["white"],
        }, {
            "other_opt": "other opt",
            "service_filters": ("combined", {
                "service_whitelist": ["white"],
            })
        }),
        ({
            "other_opt": "other opt",
            "service_blacklist": ["black"],
        }, {
            "other_opt": "other opt",
            "service_filters": ("combined", {
                "service_blacklist": ["black"],
            })
        }),
        ({
            "other_opt": "other opt",
            "service_whitelist": ["white"],
            "service_blacklist": ["black"],
        }, {
            "other_opt": "other opt",
            "service_filters": ("combined", {
                "service_whitelist": ["white"],
                "service_blacklist": ["black"],
            })
        }),
        # These params go through the transform func
        ({
            "other_opt": "other opt",
            "service_filters": "service filters",
        }, {
            "other_opt": "other opt",
            "service_filters": "service filters",
        }),
    ])
def test__transform_automatic_rediscover_parameters(parameters, result):
    assert _transform_automatic_rediscover_parameters(parameters) == result
