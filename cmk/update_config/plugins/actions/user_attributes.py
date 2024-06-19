#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from datetime import datetime
from logging import Logger

from cmk.utils.user import UserId

from cmk.gui.type_defs import Users, UserSpec
from cmk.gui.userdb import load_users, save_users

from cmk.update_config.registry import update_action_registry, UpdateAction


class UpdateUserAttributes(UpdateAction):
    def __call__(self, logger: Logger) -> None:
        users = load_users(lock=True, skip_validation=True)
        save_users(
            _update_user_attributes(logger, users),
            datetime.now(),
        )


def _add_alias(user_id: UserId, user_spec: UserSpec) -> None:
    """
    Until 2.4 the "alias" or full name could be missing for users created by LDAP.
    """
    user_spec.setdefault("alias", user_id)


def _update_user_attributes(logger: Logger, users: Users) -> Users:
    for user_id, user_spec in users.items():
        _add_alias(user_id, user_spec)
    return users


update_action_registry.register(
    UpdateUserAttributes(
        name="user_attributes",
        title="User attributes",
        # Run this validation before any plug-in that deals with users as those wouldn't be able
        # to load them.
        sort_index=2,
        # If users cannot be loaded, many other actions fail as well.
        continue_on_failure=False,
    )
)
