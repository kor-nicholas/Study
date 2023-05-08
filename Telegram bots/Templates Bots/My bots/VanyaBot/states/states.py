from aiogram.dispatcher.filters.state import StatesGroup, State

class GetInfoAboutUser(StatesGroup):
    email = State()
    phone = State()
    nick_name = State()