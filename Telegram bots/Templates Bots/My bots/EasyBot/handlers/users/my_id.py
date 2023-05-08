from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command("myid"))
async def bot_my_id(message: types.Message):
    await message.answer(f"Твой ID : {message.from_user.id}")
