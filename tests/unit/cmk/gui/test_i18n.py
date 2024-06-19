#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# pylint: disable=protected-access

# pylint: disable=redefined-outer-name

import gettext
import subprocess
from pathlib import Path

import flask
import pytest

from tests.testlib.repo import repo_path

import cmk.utils.paths

from cmk.gui import i18n
from cmk.gui.utils.script_helpers import application_and_request_context


@pytest.fixture(scope="session")
def locale_base_dir() -> Path:
    return repo_path() / "locale"


@pytest.fixture(autouse=True)
def locale_paths(tmp_path, monkeypatch, locale_base_dir):
    monkeypatch.setattr(cmk.utils.paths, "locale_dir", locale_base_dir)
    monkeypatch.setattr(cmk.utils.paths, "local_locale_dir", tmp_path / "locale")


@pytest.fixture(autouse=True, scope="session")
def compile_builtin_po_files(locale_base_dir):
    builtin_dir = locale_base_dir / "de" / "LC_MESSAGES"
    po_file = builtin_dir / "multisite.po"
    mo_file = builtin_dir / "multisite.mo"
    if po_file.exists():
        subprocess.call(["msgfmt", str(po_file), "-o", str(mo_file)])


@pytest.fixture()
def local_translation() -> None:
    _add_local_translation("de", "Äxtended German", texts={"bla": "blub"})
    _add_local_translation("xz", "Xz", texts={"bla": "blub"})
    # Add one package localization
    _add_local_translation("packages/pkg_name/de", "pkg_name German", texts={"pkg1": "lala"})


def _add_local_translation(lang, alias, texts):
    local_dir = cmk.utils.paths.local_locale_dir / lang / "LC_MESSAGES"
    local_dir.mkdir(parents=True)
    po_file = local_dir / "multisite.po"
    mo_file = local_dir / "multisite.mo"

    with (local_dir.parent / "alias").open("w", encoding="utf-8") as f:
        f.write("%s\n" % alias)

    with po_file.open(mode="w", encoding="utf-8") as f:
        f.write(
            """
msgid ""
msgstr ""
"Project-Id-Version: Locally modified Check_MK translation\\n"
"Report-Msgid-Bugs-To: checkmk-en@lists.mathias-kettner.de\\n"
"Language-Team: none\\n"
"Language: de\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\\n"
"""
        )

        for key, val in texts.items():
            f.write(
                """
msgid "%s"
msgstr "%s"
"""
                % (key, val)
            )

    subprocess.call(["msgfmt", str(po_file), "-o", str(mo_file)])


def test_underscore_without_localization(flask_app: flask.Flask) -> None:
    with flask_app.test_request_context("/"):
        assert i18n.get_current_language() == "en"
        assert isinstance(i18n._("bla"), str)
        assert i18n._("bla") == "bla"
        assert i18n._("") == ""


def test_underscore_localization(flask_app: flask.Flask) -> None:
    with application_and_request_context():
        i18n.localize("de")
        assert i18n.get_current_language() == "de"
        assert i18n._("Age") == "Alter"
        assert i18n._("") == ""

    with application_and_request_context():
        i18n._unlocalize()
        assert i18n._("Age") == "Age"
        assert i18n.get_current_language() == "en"


def test_lazy_localization() -> None:
    with application_and_request_context():
        lazy_str = i18n._l("Age")
        assert lazy_str == "Age"

    with application_and_request_context():
        i18n.localize("de")
        assert lazy_str == "Alter"

    with application_and_request_context():
        i18n._unlocalize()
        assert lazy_str == "Age"


def test_lazy_with_args() -> None:
    with application_and_request_context():
        lazy_str = i18n._l("Edit foreign %s") % "zeugs"
        assert lazy_str == "Edit foreign zeugs"

    with application_and_request_context():
        i18n.localize("de")
        assert lazy_str == "Fremde(n) zeugs editieren"

    with application_and_request_context():
        i18n._unlocalize()
        assert lazy_str == "Edit foreign zeugs"


def test_init_language_not_existing() -> None:
    assert i18n._init_language("xz") is None


def test_init_language_only_builtin(request_context: None) -> None:
    trans = i18n._init_language("de")
    assert isinstance(trans, gettext.GNUTranslations)
    assert trans.info()["language"] == "de"
    assert trans.info()["project-id-version"] == "Checkmk user interface translation 0.1"

    translated = trans.gettext("bla")
    assert isinstance(translated, str)
    assert translated == "bla"


def test_init_language_with_local_modification(
    local_translation: None, request_context: None
) -> None:
    trans = i18n._init_language("de")
    assert isinstance(trans, gettext.GNUTranslations)
    assert trans.info()["language"] == "de"
    assert trans.info()["project-id-version"] == "Locally modified Check_MK translation"

    translated = trans.gettext("bla")
    assert isinstance(translated, str)
    assert translated == "blub"


def test_init_language_with_local_modification_fallback(
    local_translation: None, request_context: None
) -> None:
    trans = i18n._init_language("de")
    assert isinstance(trans, gettext.GNUTranslations)
    assert trans.info()["language"] == "de"
    assert trans.info()["project-id-version"] == "Locally modified Check_MK translation"

    translated = trans.gettext("bla")
    assert isinstance(translated, str)
    assert translated == "blub"

    # This string is localized in the standard file, not in the locally
    # overridden file
    translated = trans.gettext("Age")
    assert isinstance(translated, str)
    assert translated == "Alter"


def test_init_language_with_package_localization(
    local_translation: None, request_context: None
) -> None:
    trans = i18n._init_language("de")
    assert trans is not None
    translated = trans.gettext("pkg1")
    assert isinstance(translated, str)
    assert translated == "lala"


def test_get_language_alias() -> None:
    assert isinstance(i18n.get_language_alias("en"), str)
    assert i18n.get_language_alias("en") == "English"

    assert isinstance(i18n.get_language_alias("de"), str)
    assert i18n.get_language_alias("de") == "German"


def test_get_language_local_alias(local_translation: None) -> None:
    assert isinstance(i18n.get_language_alias("de"), str)
    assert i18n.get_language_alias("de") == "Äxtended German"


def test_get_languages() -> None:
    assert i18n.get_languages() == [
        ("en", "English"),
        ("de", "German"),
        ("nl", "Dutch (not supported)"),
        ("fr", "French (not supported)"),
        ("it", "Italian (not supported)"),
        ("ja", "Japanese (not supported)"),
        ("pt_PT", "Portuguese (Portugal) (not supported)"),
        ("ro", "Romanian (not supported)"),
        ("es", "Spanish (not supported)"),
    ]


def test_get_languages_new_local_language(local_translation: None) -> None:
    assert i18n.get_languages() == [
        ("en", "English"),
        ("de", "Äxtended German"),
        ("nl", "Dutch (not supported)"),
        ("fr", "French (not supported)"),
        ("it", "Italian (not supported)"),
        ("ja", "Japanese (not supported)"),
        ("pt_PT", "Portuguese (Portugal) (not supported)"),
        ("ro", "Romanian (not supported)"),
        ("es", "Spanish (not supported)"),
        ("xz", "Xz"),
    ]
