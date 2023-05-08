from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.channel import channel_keyboard

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(message.from_user.username)
    await message.answer(f'Для того, чтобы воспользоваться ботом - подпишитесь на канал', reply_markup=channel_keyboard)
