from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_reply_mupkup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Тест"),
            KeyboardButton("Продукты")
        ]
    ], resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Назад")
        ]
    ],resize_keyboard=True
)

products = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Продукты")
        ]
    ],resize_keyboard=True
)