from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🛒 Rates"),
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)