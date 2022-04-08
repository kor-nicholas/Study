from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from keyboards.default.test import buy
from keyboards.inline.test_inline import buy_1
from aiogram.types import ReplyKeyboardRemove

from loader import dp


@dp.message_handler(CommandStart())
async def bot_echo(message: types.Message):
    await message.answer("Приветствующие сообщение от бота", reply_markup=buy)

@dp.message_handler(text="🛒 Rates")
async def back(message : types.Message):
    await message.answer("⬇️ Выбери сроки подписки ⬇️",reply_markup=buy_1)

@dp.message_handler(Command("myid"))
async def bot_my_id(message: types.Message):
    await message.answer(f"Твой ID : {message.from_user.id}")