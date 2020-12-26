import random
from pyrogram import Client, filters
from pyrobot import COMMAND_HAND_LER
from pyrobot.helper_functions.cust_p_filters import f_onw_fliter

GAALI_STRINGS = (
    "Teri maa ki chut bhosdike",
    "Gaand me daanda daalk tod denge madarchod",
    "yhi patak k chod denge chal nikal madharchod",
    "Abe laude aapna kaam kar",
    "chutiya hi reh jayega",
    "na chuche baate uche uche..",
    "bhosdike keh ke lenge teri aa..",
    "beta gaand mei guuda na hai teri",
    "aandha hai ka laude",
)
@Client.on_message(
    filters.command("gaali", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /gaali strings """
    effective_string = random.choice(GAALI_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

    
