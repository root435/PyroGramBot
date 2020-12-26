import random
from pyrogram import Client, filters
from pyrobot import COMMAND_HAND_LER
from pyrobot.helper_functions.cust_p_filters import f_onw_fliter


GBUN_STRINGS = (
    "Beware! This bot-admeme can gbun you right off the map.",
    "What if there was 'a' instead of 'u' ...👀",
    "I guess you've forgot spelling of gban maybe...?",
    "OK no!",
    "OK boomer.",
    "Don't misuse your powers noob...",
    "Nah, he looks innocent...",
    "Get ready for global bun hammer!",
)
@Client.on_message(
    filters.command("gbun", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /gbun strings """
    effective_string = random.choice(GBUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
