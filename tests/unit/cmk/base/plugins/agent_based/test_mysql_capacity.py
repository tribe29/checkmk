#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2022 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
from typing import Callable

import pytest

from cmk.base.api.agent_based.checking_classes import Metric, Result, Service, State
from cmk.base.plugins.agent_based import mysql_capacity


@pytest.fixture(name="check")
def _check(fix_register) -> Callable:
    return mysql_capacity.check_mysql_size


@pytest.fixture(name="discovery")
def _discovery(fix_register) -> Callable:
    return mysql_capacity.discover_mysql_size


def test_discovery(discovery):
    section = {
        "mysql": {
            "red": (12, 0),
            "information_schema": (12, 0),
            "performance_schema": (12, 0),
            "mysql": (12, 0),
        }
    }
    assert list(discovery(section)) == [Service(item="mysql:red")]


def test_check(check):
    item = "mysql:reddb"
    params = {"levels": (None, None)}
    section = {"mysql": {"reddb": (42, 0)}}
    assert list(check(item=item, params=params, section=section)) == [
        Result(state=State.OK, summary="Size: 42 B"),
        Metric("database_size", 42.0),
    ]
