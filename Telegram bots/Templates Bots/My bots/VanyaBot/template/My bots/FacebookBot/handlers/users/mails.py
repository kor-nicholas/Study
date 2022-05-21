from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states.state import Mails

from sql.sql_db import SQL_people
from data.config import db_sql

@dp.message_handler(commands=['mail'])
async def mail_input(message: types.Message):
    await message.answer("Введите сообщение для рассылки")
    await Mails.mess.set()

@dp.message_handler(state=Mails.mess)
async def mail_send(message: types.Message, state: FSMContext):
    mess = message.text
    await state.finish()

    sql_object = SQL_people(db_sql)

    for id in sql_object.mailing():
        await message.bot.send_message(id[0], mess) # id[0] - telegram_id каждой строчки в таблице

    sql_object.sql_close()

    await message.answer("Рассылка окончена успешно")