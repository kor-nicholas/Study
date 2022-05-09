from aiogram.dispatcher.filters.state import StatesGroup, State

class Test(StatesGroup): # группа состояний (сколько будет вопросов) + наследование от класса StatesGroup
    Q1 = State() # вопрос 1 (State - фильтр, для хендлера)
    Q2 = State() # вопрос 2 (State - фильтр, для хендлера)