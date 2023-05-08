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