#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2020 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

import pytest

from cmk.base.plugins.agent_based.utils.docker import parse, parse_multiline, _cleanup_oci_error_message


def test_parse_strict():
    result = parse([[
        "@docker_version_info",
        '{"PluginVersion": "0.1", "DockerPyVersion": "4.1.0", "ApiVersion": "1.41"}'
    ], ['{"payload": 1}']])
    assert result.version == {
        "PluginVersion": "0.1",
        "DockerPyVersion": "4.1.0",
        "ApiVersion": "1.41"
    }
    assert result.data == {"payload": 1}


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            [["@docker_version_info", "{}"], ["1", "2"]],  # 2 should not be there
            1),
        (
            [["@docker_version_info", "{}", "2"], ["1"]],  # 2 should not be there
            1),
        (
            [["@docker_version_info", "{}"], ["1"], ["2"]],  # 2 should not be there
            1),
    ])
def test_parse_strict_violation(data, expected):
    with pytest.raises(ValueError):
        parse(data)
    assert parse(data, strict=False).data == expected


def test_parse_strict_empty_version():
    result = parse([["@docker_version_info", "{}"], ['{"payload": 1}']])
    assert result.version == {}
    assert result.data == {"payload": 1}


def test_parse_multiline():
    result = parse_multiline([["@docker_version_info", "{}"], ['{"value": 1}'], ['{"value": 2}'],
                              ['{"value": 3}']])
    assert result.version == {}
    assert list(result.data) == [{"value": 1}, {"value": 2}, {"value": 3}]


@pytest.mark.parametrize(
    "data_in, data_out",
    [
        (
            [],
            [],
        ),
        (
            [["1"]],
            [["1"]],
        ),
        (
            [["1", "2"]],
            [["1", "2"]],
        ),
        (
            # this is the original error message
            [["1", "2"],
             [
                 'OCI runtime exec failed: exec failed: container_linux.go:344: starting container '
                 'process caused "exec: \"check_mk_agent\": executable file not found in $PATH": unknown'
             ]],
            [["1", "2"]],
        ),
        (
            # this is the prefix it is tested with
            [["1", "2"], ['OCI runtime exec failed: exec failed:']],
            [["1", "2"]],
        ),
        (
            # only replace if last element is of size 1
            [["1", "2"], ['1', 'OCI runtime exec failed: exec failed:']],
            [["1", "2"], ['1', 'OCI runtime exec failed: exec failed:']],
        ),
    ])
def test_parse_remove_error_message(data_in, data_out):
    cleaned_up = _cleanup_oci_error_message(data_in)
    assert cleaned_up == data_out
