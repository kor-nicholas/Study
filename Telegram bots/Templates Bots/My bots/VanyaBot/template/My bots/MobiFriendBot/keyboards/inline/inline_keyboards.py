from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import manager_username

category = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Телефони', callback_data='phone')
        ],
        [
            InlineKeyboardButton('Навушники', callback_data='headphones')
        ],
        [
            InlineKeyboardButton('Часи', callback_data='clock')
        ],
        [
            InlineKeyboardButton('Камери', callback_data='cameras')
        ],
        [
            InlineKeyboardButton('Рiзне', callback_data='other')
        ],
        [
            InlineKeyboardButton('Назад', callback_data='back')
        ]
    ]
)

manager = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Написати менеджеру', url=f'tg://resolve?domain={manager_username}'),
            InlineKeyboardButton('Назад', callback_data='back')
        ]
    ]
)

products = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Замовити', callback_data='buy'),
        ]
    ]
)

send_order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Вiдправити заявку', callback_data='send')
        ]
    ]
)

back_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Назад', callback_data='back')
        ]
    ]
)