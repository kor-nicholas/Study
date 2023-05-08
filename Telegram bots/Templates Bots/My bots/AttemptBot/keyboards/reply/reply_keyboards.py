from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Новый заказ 🍽'),
            KeyboardButton('Связаться с оператором 📞')
        ],
        [
            KeyboardButton('Акции и скидки 🎉'),
            KeyboardButton('Корзина 🛒')
        ]
    ],resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Назад')
        ]
    ],resize_keyboard=True,one_time_keyboard=True
)