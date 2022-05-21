from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from sql.sql_db import SQL_product
from data.config import db_sql

from states.state import Add

# Команда для добавления товара в Список товаров
@dp.message_handler(commands=['add'])
async def add(message: types.Message):
    await message.answer("Введите название: ")
    await Add.name.set()

@dp.message_handler(state=Add.name)
async def name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите описание: ")
    await Add.description.set()

@dp.message_handler(state=Add.description)
async def desc(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите цену: ")
    await Add.prise.set()

@dp.message_handler(state=Add.prise)
async def prise(message: types.Message, state: FSMContext):
    await state.update_data(prise=message.text)
    await message.answer("Отправьте фотографию: ")
    await Add.photo_id.set()

@dp.message_handler(content_types=['photo'], state=Add.photo_id)
async def photo(message : types.Message, state: FSMContext):
    await state.update_data(photo_id=message.photo[-1].file_id)
    await message.answer("Введите количество товаров: ")
    await Add.count.set()

@dp.message_handler(state=Add.count)
async def count(message : types.Message, state: FSMContext):
    await state.update_data(count=message.text)
    adds = await state.get_data()

    # Добавляем данные о товаре в базу
    sql_object = SQL_product(db_sql)
    sql_object.sql_add_product(adds['name'], adds['description'], adds['prise'], adds['photo_id'], adds['count'])
    sql_object.sql_close()

    await state.finish()
    await message.answer("Товар добавлен в Список товаров")