from aiogram.dispatcher.filters.state import StatesGroup, State

class Test(StatesGroup):
    addres = State()
    more_info = State()