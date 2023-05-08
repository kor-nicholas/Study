from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import URL

buy_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Месяц",callback_data="month")
        ],
        [
            InlineKeyboardButton("Год", callback_data="year")
        ]
    ]
)

buy_2_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Visa/MasterCard", callback_data='visa1')
        ],
        [
            InlineKeyboardButton("Назад", callback_data="back_main")
        ]
    ]
)

buy_2_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Visa/MasterCard", callback_data='visa2')
        ],
        [
            InlineKeyboardButton("Назад", callback_data="back_main")
        ]
    ]
)

buy_visa_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Я оплатил",callback_data='complete1')
        ],
        [
            InlineKeyboardButton("Отменить", callback_data='back2_1_1')
        ]
    ]
)

buy_visa_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Я оплатил",callback_data='complete2')
        ],
        [
            InlineKeyboardButton("Отменить", callback_data='back2_1_2')
        ]
    ]
)