from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_buy_link = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Оплатить", url="privatbank.com")
    ]
])