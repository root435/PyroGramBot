import random
from pyrogram import Client, filters
from pyrobot import COMMAND_HAND_LER
from pyrobot.helper_functions.cust_p_filters import f_onw_fliter

GYAAN_STRINGS = (
    "Attitude is a choice. Happiness is a choice. Optimism is a choice. Kindness is a choice. Giving is a choice. Respect is a choice. Whatever choice you make makes you. Choose wisely.",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "Instead of worrying about what you cannot control, shift your energy to what you can create",
    "It’s only after you’ve stepped outside your comfort zone that you begin to change, grow, and transform.",
    "More smiling, less worrying. More compassion, less judgment. More blessed, less stressed. More love, less hate",
    "Take responsibility of your own happiness, never put it in other people’s hands.",
    "If you want to be happy, do not dwell in the past, do not worry about the future, focus on living fully in the present.",
    "Success is going from failure to failure without losing your enthusiasm",
    "The journey of a thousand miles begins with one step.",
    "Tough times never last, but tough people do.",
    "Keep your face to the sunshine and you can never see the shadow.",
    "There is only one success: to be able to spend your life in your own way.",
    "The best way out is always through.",
    "The power of imagination makes us infinite.",
    "Make each day your masterpiece.",
    "The best dreams happen when you’re awake.",
    "Once you choose hope, anything’s possible.",
    "Every moment is a fresh beginning.",
    "Believe and act as if it were impossible to fail.",
    "Don’t count the days, make the days count.",
    "The difference between ordinary and extraordinary is that little extra.",
    "You must not only aim right, but draw the bow with all your might.",
    "Light tomorrow with today.",
    "Even if you’re on the right track, you’ll get run over if you just sit there.",
)
@Client.on_message(
    filters.command("gyaan", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /gyaan strings """
    effective_string = random.choice(GYAAN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)

    
