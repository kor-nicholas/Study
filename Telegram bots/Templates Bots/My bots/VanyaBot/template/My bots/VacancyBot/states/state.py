from aiogram.dispatcher.filters.state import StatesGroup, State

class Mails(StatesGroup):
    mess = State()

class Add_category(StatesGroup):
    name = State()

class Delete_category(StatesGroup):
    name = State()

class Add_vacancy(StatesGroup):
    category = State()
    name = State()
    description = State()
    salary = State()

class Delete_vacancy(StatesGroup):
    category = State()
    name = State()

class Change(StatesGroup):
    id = State()
    input = State()
    value = State()
    photo_id = State()

class Order(StatesGroup):

    # Информация о пользователе
    other_category = State()
    telegram_id = State()
    fio = State()
    email = State()
    phone = State()
    social_network = State()
    education = State()
    experience = State()
    foreign_language = State()
    doc = State()
    other_info = State()

    # Подтверждения отправки заявки
    confirm_send = State()