from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопка подтверждения что прочитанный Информационный раздел(FAQ)
read = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Я прочитал ✅', callback_data='read')
        ]
    ]
)

# Кнопка Оформить заказ
order_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Оформить заказ', callback_data='order')
        ]
    ]
)

# Кнопка для связи со мной
feedback = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Написать', url="https://t.me/kostyabog145")
        ]
    ]
)

