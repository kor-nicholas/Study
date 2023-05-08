from aiogram import types

from loader import dp


@dp.message_handler(commands=['myid'])
async def bot_start(message: types.Message):
    await message.answer(f"Твой ID: {message.from_user.id}")
    await message.answer(f"ID группы: {message.chat.id}")

