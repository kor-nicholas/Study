from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from sql.sql_db import SQL_category
from data.config import db_sql

from states.state import Delete_category


# Команда для удаления категории из базы
@dp.message_handler(commands=['delete_category'])
async def add(message: types.Message):

    await message.answer("Введите название категории: ")
    await Delete_category.name.set()

@dp.message_handler(state=Delete_category.name)
async def name(message: types.Message, state: FSMContext):

    # Удаляем из базы категорию
    sql_object = SQL_category(db_sql)
    sql_object.delete_category(message.text)
    sql_object.sql_close()

    await state.finish()
    await message.answer("Категория удалена")