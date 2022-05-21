from aiogram.dispatcher.filters.state import StatesGroup, State

class Add(StatesGroup):
    name = State()
    category = State()
    description = State()
    photo_id = State()
    prise = State()
    code = State()

class Delete(StatesGroup):
    name = State()
    prise = State()

class Order(StatesGroup):
    order_username = State()
    order_code = State()
    order_name = State()
    order_first_name = State()
    order_city = State()
    order_country = State()
    order_post = State()
    order_phone = State()

class Find_code(StatesGroup):
    code = State()
