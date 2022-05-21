from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from sql.sql_db import SQL_category
from data.config import db_sql

from states.state import Add_category

# Команда для добавления категории в базу
@dp.message_handler(commands=['add_category'])
async def add(message: types.Message):
    await message.answer("Введите название категории: ")
    await Add_category.name.set()

@dp.message_handler(state=Add_category.name)
async def name(message: types.Message, state: FSMContext):

    # Добавляем в базу категорию
    sql_object = SQL_category(db_sql)
    sql_object.add_category(message.text)
    sql_object.sql_close()

    await state.finish()
    await message.answer("Категория добавлена")