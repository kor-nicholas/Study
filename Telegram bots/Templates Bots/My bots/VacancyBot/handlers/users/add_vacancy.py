from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from sql.sql_db import SQL_vacancy
from data.config import db_sql

from states.state import Add_vacancy


# Команда для добавления вакансии в базу
@dp.message_handler(commands=['add_vacancy'])
async def add(message: types.Message):
    await message.answer("Введите категорию вакансии: ")
    await Add_vacancy.category.set()

@dp.message_handler(state=Add_vacancy.category)
async def add_category(message: types.Message, state: FSMContext):

    await state.update_data(category=message.text)
    await message.answer("Введите название вакансии: ")
    await Add_vacancy.name.set()

@dp.message_handler(state=Add_vacancy.name)
async def add_name(message: types.Message, state: FSMContext):

    await state.update_data(name=message.text)
    await message.answer("Введите описание вакансии: ")
    await Add_vacancy.description.set()

@dp.message_handler(state=Add_vacancy.description)
async def add_desc(message: types.Message, state: FSMContext):

    await state.update_data(description=message.text)
    await message.answer("Введите запрлату вакансии: ")
    await Add_vacancy.salary.set()


@dp.message_handler(state=Add_vacancy.salary)
async def add_salary(message: types.Message, state: FSMContext):

    await state.update_data(salary=int(message.text))
    info = await state.get_data()
    await state.finish()

    sql_object = SQL_vacancy(db_sql)
    sql_object.add_vacancy(info['category'], info['name'], info['description'], int(info['salary']))
    sql_object.sql_close()

    print(info)

    await message.answer("Вакансия добавлена")
