from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

type_order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Доставка',callback_data='type_order')
        ]
    ]
)

yes_or_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Да', callback_data='yes'),
            InlineKeyboardButton('Нет',callback_data='no')
        ]
    ]
)

to_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Меню', callback_data='menu')
        ]
    ]
)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Выпечка', callback_data='bakery'),
            InlineKeyboardButton('Гарнир', callback_data='garnish'),
            InlineKeyboardButton('Горячие мясные', callback_data='hot_meat')
        ],
        [
            InlineKeyboardButton('Напитки', callback_data='drink'),
            InlineKeyboardButton('Первые блюда', callback_data='first_eat'),
            InlineKeyboardButton('Салаты', callback_data='salat')
        ],
        [
            InlineKeyboardButton('Соус', callback_data='sauce'),
            InlineKeyboardButton('Холодная закуска', callback_data='cold_eat')
        ]
    ]
)

bakerys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Булочки', callback_data='backery_1'),
            InlineKeyboardButton('Хачапури по м...', callback_data='backery_2'),
            InlineKeyboardButton('Хачапури по а...', callback_data='backery_3'),
        ],
        [
            InlineKeyboardButton('Хачапури со ш...', callback_data='backery_4'),
            InlineKeyboardButton('Хачапури по ц...', callback_data='backery_5'),
            InlineKeyboardButton('Хачапури по и...', callback_data='backery_6')
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)

garnishs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Том Ям с морепродуктами', callback_data='garnish_1')
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)

hot_meats = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Курочка из элитного района Суела', callback_data='hot_meats_1')
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)

drinks = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Большой Чикен', callback_data='drink_1')
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)

salats = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Салат Чики-чикен', callback_data='salat_1')
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)

cold_eats = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Онигири', callback_data='cold_eat_1')
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)


















a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
prise_a = 490
prise_b = 320
prise_c = 642
prise_d = 146
prise_e = 856
prise_f = 434

bakerys_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('-', callback_data='-'),
            InlineKeyboardButton(f'{a} шт', callback_data='now'),
            InlineKeyboardButton('+', callback_data='+'),
        ],
        [
            InlineKeyboardButton(f'В корзину: {prise_a*a}', callback_data='basket'),
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)

garnishs_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('-', callback_data='-'),
            InlineKeyboardButton(f'{b} шт', callback_data='now'),
            InlineKeyboardButton('+', callback_data='+'),
        ],
        [
            InlineKeyboardButton(f'В корзину: {prise_b*b}', callback_data='basket'),
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)

hot_meats_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('-', callback_data='-'),
            InlineKeyboardButton(f'{c} шт', callback_data='now'),
            InlineKeyboardButton('+', callback_data='+'),
        ],
        [
            InlineKeyboardButton(f'В корзину: {prise_c*c}', callback_data='basket'),
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)

drinks_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('-', callback_data='-'),
            InlineKeyboardButton(f'{d} шт', callback_data='now'),
            InlineKeyboardButton('+', callback_data='+'),
        ],
        [
            InlineKeyboardButton(f'В корзину: {prise_d*d}', callback_data='basket'),
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)

salats_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('-', callback_data='-'),
            InlineKeyboardButton(f'{e} шт', callback_data='now'),
            InlineKeyboardButton('+', callback_data='+'),
        ],
        [
            InlineKeyboardButton(f'В корзину: {prise_e*e}', callback_data='basket'),
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)

cold_eats_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('-', callback_data='-'),
            InlineKeyboardButton(f'{f} шт', callback_data='now'),
            InlineKeyboardButton('+', callback_data='+'),
        ],
        [
            InlineKeyboardButton(f'В корзину: {prise_f*f}', callback_data='basket'),
        ],
        [
            InlineKeyboardButton('Назад в меню', callback_data='back')
        ]
    ]
)
