from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from sql.sql_db import SQL_vacancy
from data.config import db_sql

from states.state import Delete_vacancy


# Команда для удаления вакансии из базы
@dp.message_handler(commands=['delete_vacancy'])
async def delete(message: types.Message):
    await message.answer("Введите категорию вакансии: ")
    await Delete_vacancy.category.set()


@dp.message_handler(state=Delete_vacancy.category)
async def delete_category(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer("Введите название вакансии: ")
    await Delete_vacancy.name.set()


@dp.message_handler(state=Delete_vacancy.name)
async def delete_name(message: types.Message, state: FSMContext):

    await state.update_data(name=message.text)
    info = await state.get_data()
    await state.finish()

    sql_object = SQL_vacancy(db_sql)
    sql_object.delete_vacancy(info['category'], info['name'])
    sql_object.sql_close()

    print(info)

    await message.answer("Вакансия удалена")