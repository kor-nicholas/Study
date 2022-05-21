from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import username

start_murkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Мой профиль", callback_data="profil")
        ],
        [
            InlineKeyboardButton("Покупка", callback_data="buy")
        ],
        [
            InlineKeyboardButton("Правила", callback_data="rules")
        ],
        [
            InlineKeyboardButton("Помощь", url=f"tg://resolve?domain={username}")
        ]
    ]
)

back_murkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Назад", callback_data="back")
        ]
    ]
)

log_murkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Log fb usa", callback_data="usa"),
            InlineKeyboardButton("Log fb mix", callback_data="mix")
        ]
        ,[
            InlineKeyboardButton("Назад", callback_data="back")
        ]
    ]
)