from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import GROUP_URL

channel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Подписаться на канал', url=GROUP_URL)],
        [InlineKeyboardButton('Я подписался ✅ ', callback_data='check_subcscribe')]
    ]
)


