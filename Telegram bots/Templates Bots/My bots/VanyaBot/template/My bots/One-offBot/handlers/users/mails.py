from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states.state import Mails

from sql.sql_db import SQL_people
from data.config import db_sql

# Команда /mail - рассылка
@dp.message_handler(commands=['mail'])
async def mail_input(message: types.Message):

    # Просим сообщение для рассылки
    await message.answer("Введите сообщение для рассылки")
    await Mails.mess.set()

@dp.message_handler(state=Mails.mess)
async def mail_send(message: types.Message, state: FSMContext):

    # Сохраняем в Стейт сообщение, которое будем всем отсылать
    mess = message.text
    await state.finish()

    # Достаем из базы все telegram_id людей
    sql_object = SQL_people(db_sql)
    array_id = sql_object.mailing()
    sql_object.sql_close()

    # Рассылаем каждому сообщение из Стейта
    for id in array_id:
        await message.bot.send_message(id[0], mess) # id[0] - telegram_id каждой строчки в таблице

    await message.answer("Рассылка окончена успешно")