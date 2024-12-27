from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    message = await message.bot.send_message(-1002276963350, 'test')
    print(message['message_id'])
    await message.bot.edit_message_text('new text', -1002276963350, message['message_id'])
