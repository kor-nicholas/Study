from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import feedback_nick

feedback = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Написать поддержке', url=f't.me/{feedback_nick}')
        ]
    ]
)