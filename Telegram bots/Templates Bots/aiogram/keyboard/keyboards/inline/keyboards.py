from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import url_pear, url_apple

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Купить грушу",callback_data="pear"),
            InlineKeyboardButton("Купить яблоко", callback_data="apple")
        ],
        [
            InlineKeyboardButton('Написати менеджеру', url=f'tg://resolve?domain={config.supportusid}')
        ],
        [
            InlineKeyboardButton("Отмена",callback_data="cancel")
        ]
    ]
)

pear_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Купи тут", url=url_pear)
        ]
    ]
)

apple_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Купи тут", url=url_apple)
        ]
    ]
)

