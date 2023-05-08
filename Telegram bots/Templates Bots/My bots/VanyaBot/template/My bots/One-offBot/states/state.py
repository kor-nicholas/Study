from aiogram.dispatcher.filters.state import StatesGroup, State

class Mails(StatesGroup):
    mess = State()

class Add(StatesGroup):
    name = State()
    description = State()
    photo_id = State()
    prise = State()
    count = State()

class Delete(StatesGroup):
    name = State()
    prise = State()

class Input(StatesGroup):
    delete = State()

class Change(StatesGroup):
    id = State()
    input = State()
    value = State()
    photo_id = State()

class Order(StatesGroup):

    # Информация о пользователе
    telegram_id = State() #
    fio = State() #
    phone = State() #
    city = State()  #
    get_product = State() #
    post_office = State() #
    date = State() #
    clock = State() #

    # Подтверждения отправки заявки
    confirm_send = State()