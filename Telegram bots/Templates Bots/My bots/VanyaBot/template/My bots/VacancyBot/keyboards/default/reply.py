from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура при /start
start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Вакансии')
        ],
        [
            KeyboardButton('О нас'),
            KeyboardButton('Контакты')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Назад')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

confirm_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Подтвердить ✅'),
            KeyboardButton('Переоформить заказ ❌')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)