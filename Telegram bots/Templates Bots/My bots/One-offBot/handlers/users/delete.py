from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from sql.sql_db import SQL_product
from data.config import db_sql

from states.state import Delete

# Удаление товара из Списка товаров
@dp.message_handler(commands=['delete'])
async def add(message: types.Message):
    await message.answer("Введите название: ")
    await Delete.name.set()

@dp.message_handler(state=Delete.name)
async def name_del(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите цену: ")
    await Delete.prise.set()

@dp.message_handler(state=Delete.prise)
async def prise_del(message: types.Message, state: FSMContext):
    await state.update_data(prise=message.text)
    dels = await state.get_data()

    # Удаление данных о товаре из базы
    sql_object = SQL_product(db_sql)
    sql_object.sql_delete_product(dels['name'], dels['prise'])
    sql_object.sql_close()

    await state.finish()
    await message.answer("Товар удален из Списка товаров")