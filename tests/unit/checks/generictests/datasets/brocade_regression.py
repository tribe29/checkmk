#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

# yapf: disable
# type: ignore

checkname = 'brocade_fcport'

info = [
    [
        [
            u'1', u'4', u'2', u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0',
            u'0', u'15', u'5', u'del_EVA6000_A2'
        ],
        [
            u'2', u'6', u'1', u'1', u'1215057779', u'3341142793',
            u'2315846346', u'3778522298', u'2869057944', u'0', u'0', u'6',
            u'0', u'4', u'ISL_fswf01_Port_1'
        ],
        [
            u'3', u'4', u'2', u'2', u'9770', u'3220', u'675', u'135', u'0',
            u'0', u'0', u'3', u'0', u'5', u'del_fsvdb06_R'
        ],
        [
            u'4', u'6', u'1', u'1', u'1766254627', u'4035913760', u'344812533',
            u'195005757', u'0', u'0', u'72', u'22486', u'47', u'4',
            u'fsvmg01_R'
        ]
    ], [[u'2', u'64'], [u'24', u'64']],
    [
        [u'805306369', u'6', u'100'], [u'805306370', u'24', u'0'],
        [u'805306371', u'131', u'0'], [u'805306372', u'1', u'0'],
        [u'805306373', u'1', u'0'], [u'805306374', u'1', u'0'],
        [u'1073741824', u'56', u'8000'], [u'1073741825', u'56', u'4000'],
        [u'1073741826', u'56', u'8000'], [u'1073741827', u'56', u'4000']
    ],
    [
        ['16.0.0.5.30.93.171.142.0.0.0.0.0.0.0.0.1', [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 51, 32, 55, 52, 32, 56, 56, 32, 70, 66, 32, 48, 48], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 51, 32, 50, 48, 32, 65, 54, 32, 48, 51, 32, 66, 56], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48],],
        ['16.0.0.5.30.93.171.142.0.0.0.0.0.0.0.0.2', [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 67, 32, 56, 70, 32, 55, 48, 32, 68, 68, 32, 55, 52], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 50, 32, 69, 50, 32, 69, 67, 32, 53, 55, 32, 50, 66], [48, 48, 32, 48, 48, 32, 53, 66, 32, 66, 54, 32, 65, 70, 32, 51, 67, 32, 70, 56, 32, 51, 52], [48, 48, 32, 48, 48, 32, 49, 51, 32, 57, 70, 32, 51, 67, 32, 69, 67, 32, 69, 66, 32, 57, 67], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 65, 66, 32, 49, 49, 32, 54, 51, 32, 66, 57],],
        ['16.0.0.5.30.93.171.142.0.0.0.0.0.0.0.0.3', [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 50, 32, 65, 51], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 56, 55], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 57, 56, 32, 65, 56], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 51, 50, 32, 53, 48], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48],],
        ['16.0.0.5.30.93.171.142.0.0.0.0.0.0.0.0.4', [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 56, 32, 49, 52, 32, 56, 68, 32, 70, 67, 32, 50, 51], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 56, 32, 48, 66, 32, 57, 70, 32, 68, 57, 32, 66, 66], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 53, 32, 65, 53, 32, 51, 70, 32, 48, 69, 32, 56, 52], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 51, 32, 67, 50, 32, 53, 48, 32, 69, 53, 32, 50, 48], [48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32, 48, 48, 32,
                                                                                48, 48],],
    ]
]

discovery = {
    '': [
        (
            u'1 ISL ISL_fswf01_Port_1',
            '{ "phystate": [6], "opstate": [1], "admstate": [1] }'
        ),
        (
            u'3 fsvmg01_R',
            '{ "phystate": [6], "opstate": [1], "admstate": [1] }'
        )
    ]
}

checks = {
    '': [
        (
            u'1 ISL ISL_fswf01_Port_1', {
                'assumed_speed': 2.0,
                'phystate': [6],
                'notxcredits': (3.0, 20.0),
                'opstate': [1],
                'c3discards': (3.0, 20.0),
                'admstate': [1],
                'rxencinframes': (3.0, 20.0),
                'rxcrcs': (3.0, 20.0),
                'rxencoutframes': (3.0, 20.0)
            }, [
                (
                    0,
                    'ISL speed: 4 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
                    [
                        ('in', 0.0, None, None, 0, 400000000.0),
                        ('out', 0.0, None, None, 0, 400000000.0),
                        ('rxframes', 0.0, None, None, None, None),
                        ('txframes', 0.0, None, None, None, None),
                        ('rxcrcs', 0.0, None, None, None, None),
                        ('rxencoutframes', 0.0, None, None, None, None),
                        ('rxencinframes', 0.0, None, None, None, None),
                        ('c3discards', 0.0, None, None, None, None),
                        ('notxcredits', 0.0, None, None, None, None),
                        ('fc_bbcredit_zero', 0.0, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            u'3 fsvmg01_R', {
                'assumed_speed': 2.0,
                'phystate': [6],
                'notxcredits': (3.0, 20.0),
                'opstate': [1],
                'c3discards': (3.0, 20.0),
                'admstate': [1],
                'rxencinframes': (3.0, 20.0),
                'rxcrcs': (3.0, 20.0),
                'rxencoutframes': (3.0, 20.0)
            }, [
                (
                    0,
                    'Speed: 4 Gbit/s, In: 0.00 B/s, Out: 0.00 B/s, Physical: in sync, Operational: online, Administrative: online',
                    [
                        ('in', 0.0, None, None, 0, 400000000.0),
                        ('out', 0.0, None, None, 0, 400000000.0),
                        ('rxframes', 0.0, None, None, None, None),
                        ('txframes', 0.0, None, None, None, None),
                        ('rxcrcs', 0.0, None, None, None, None),
                        ('rxencoutframes', 0.0, None, None, None, None),
                        ('rxencinframes', 0.0, None, None, None, None),
                        ('c3discards', 0.0, None, None, None, None),
                        ('notxcredits', 0.0, None, None, None, None),
                        ('fc_bbcredit_zero', 0.0, None, None, None, None)
                    ]
                )
            ]
        )
    ]
}
