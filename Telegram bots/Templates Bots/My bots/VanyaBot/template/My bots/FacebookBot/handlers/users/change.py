from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from sql.sql_db import SQL_product
from data.config import db_sql

from states.state import Change

@dp.message_handler(commands=['change'])
async def change(message: types.Message):
    sql_object = SQL_product(db_sql)
    all_products = sql_object.sql_select_all()

    # [0] - id ; [1] - name ; [2] - description ; [3] - prise ; [4] - photo_id ; [5] - count
    for product in all_products:
        await message.answer(product)

    await message.answer("Введите ID товара, которого хотите изменить: ")
    await Change.id.set()

@dp.message_handler(state=Change.id)
async def change_id(message: types.Message, state: FSMContext):
    await state.update_data(id=message.text)

    await message.answer("1 - Название\n2 - Описание\n3 - Цена\n4 - Фото\n5 - Количество")

    await message.answer("Введите номер пункта, который хотите поменять: ")
    await Change.input.set()

@dp.message_handler(state=Change.input)
async def change_input(message: types.Message, state: FSMContext):
    await state.update_data(input=message.text)

    if message.text == '4':
        await message.answer("Пришлите боту фотографию, на которую хотите изменить: ")
        await Change.photo_id.set()
    else:
        await message.answer("Введите значение на которое хотите поменять: ")
        await Change.value.set()

@dp.message_handler(state=Change.value)
async def change_value(message: types.Message, state: FSMContext):
    await state.update_data(value=message.text)

    info = await state.get_data()

    sql_object = SQL_product(db_sql)

    # ['id'] - id (товара, которого меняем) ; ['input'] - что именно меняем (номер по высше порядку)
    # ['value'] - значение на которое меняем
    if int(info['input']) == 1:
        sql_object.sql_change_name_for_id(info['id'], info['value'])
        await message.answer("Название отредактировано")
    elif int(info['input']) == 2:
        sql_object.sql_change_description_for_id(info['id'], info['value'])
        await message.answer("Описание отредактировано")
    elif int(info['input']) == 3:
        sql_object.sql_change_prise_for_id(info['id'], int(info['value']))
        await message.answer("Цена отредактирована")
    elif int(info['input']) == 5:
        sql_object.sql_change_count_for_id(info['id'], int(info['value']))
        await message.answer("Количество отредактировано")
    else:
        await message.answer("Вы ввели неправильный номер для изменений")

    sql_object.sql_close()

    await state.finish()

@dp.message_handler(content_types=['photo'], state=Change.photo_id)
async def change_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo_id=message.photo[-1].file_id)

    info = await state.get_data()

    sql_object = SQL_product(db_sql)
    sql_object.sql_change_photo_id_for_id(info['id'], info['photo_id'])
    sql_object.sql_close()

    await state.finish()

    await message.answer("Фото отредактировано")