from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.reply import start

from loader import dp

from sql.sql_db import SQL_people
from data.config import db_sql

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    # Добавляем человека в базу (read = '-', так как человек не прочитал правила)
    
    sql_object = SQL_people(db_sql)
    sql_object.add_id_in_base(str(message.from_user.id))
    sql_object.sql_close()

    await message.answer(f"Приветствуеще сообщение, {message.from_user.full_name}", reply_markup=start)


