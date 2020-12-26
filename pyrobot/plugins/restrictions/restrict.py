from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    ChatPermissions
)
from pyrobot import COMMAND_HAND_LER
from pyrobot.helper_functions.admin_check import admin_check
from pyrobot.helper_functions.extract_user import extract_user
from pyrobot.helper_functions.string_handling import extract_time


@Client.on_message(filters.command("mute", COMMAND_HAND_LER))
async def mute_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    user_id, user_first_name = extract_user(message)

    try:
        await message.chat.restrict_member(
            user_id=user_id,
            permissions=ChatPermissions(
            )
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                " shhh.. quiet now "
                f"{user_first_name}"
                " mouth is shut! 🤐"
            )
        else:
            await message.reply_text(
                "👍🏻 "
                f"<a href='tg://user?id={user_id}'>"
                "Lavender"
                "</a>"
                " The mouth is closed! 🤐"
            )


@Client.on_message(filters.command("tmute", COMMAND_HAND_LER))
async def temp_mute_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return

    if not len(message.command) > 1:
        return

    user_id, user_first_name = extract_user(message)

    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        await message.reply_text(
            (
                "Invalid time type specified."
                 "Expected m, h, or d, obtained: {}"
            ).format(
                message.command[1][-1]
            )
        )
        return

    try:
        await message.chat.restrict_member(
            user_id=user_id,
            permissions=ChatPermissions(
            ),
            until_date=until_date_val
        )
    except Exception as error:
        await message.reply_text(
            str(error)
        )
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(
                "shhh... quiet now! 😠"
                f"{user_first_name}"
                f" muted for {message.command[1]}!"
            )
        else:
            await message.reply_text(
                "shhh... quiet now! 😠"
                f"<a href='tg://user?id={user_id}'>"
                "Of Lavender"
                "</a>"
                " Mouth "
                f" muted for {message.command[1]}!"
            )
