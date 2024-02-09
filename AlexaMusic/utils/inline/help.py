# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AlexaMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["S_B_1"], callback_data=f"settings_back_helper")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="‹ اوامر القنوات ›",
                    callback_data="help_callback hb1",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="‹ اوامر المجموعات ›",
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="‹ اوامر بالانگليزي ›",
                    callback_data="help_callback hb3",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_1"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["S_B_8"], callback_data=f"settingsback_helper"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
