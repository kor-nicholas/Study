from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Список товаров 🔽'),
            KeyboardButton('Корзина 🛒')
        ],
        [
            KeyboardButton('Информационный раздел ℹ')
        ]
    ],resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('🔙 Назад')
        ]
    ],resize_keyboard=True
)

shop_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Удалить из корзины по номеру'),
            KeyboardButton('Очистить корзину 🧹')
        ],
        [
            KeyboardButton('🔙 Назад')
        ]
    ], resize_keyboard=True
)

back_shop = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('🔙 Вернуться в корзину')
        ]
    ], resize_keyboard=True
)

get_product_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Почта 🚚'),
            KeyboardButton('Самовывоз 🚴‍♂️')
        ]
    ], resize_keyboard=True
)

confirm_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Подтвердить ✅'),
            KeyboardButton('Переоформить заказ ❌')
        ]
    ], resize_keyboard=True
)

