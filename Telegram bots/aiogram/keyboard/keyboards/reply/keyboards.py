from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Купить"),
            KeyboardButton("Продать")
        ],
        [
            KeyboardButton("Назад")
        ]
    ], resize_keyboard=True
)