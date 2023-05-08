from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Про магазин'),
            KeyboardButton('Контакти'),
            KeyboardButton('Пiдтримка')
        ],
        [
            KeyboardButton('Список товару'),
        ],
        [
            KeyboardButton('Бонуси (скидки)')
        ]
    ],resize_keyboard=True,one_time_keyboard=True
)

back_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Назад')
        ]
    ],resize_keyboard=True,one_time_keyboard=True
)

