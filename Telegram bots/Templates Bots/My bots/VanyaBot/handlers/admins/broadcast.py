from aiogram import types

from loader import dp

from data.config import ADMINS

@dp.message_handler(commands='broadcast')
async def broadcast(message: types.Message):
    if f'{message.from_user.id}' in ADMINS:
        await message.answer('Введите информацию пользователям')
    else:
        await message.answer('Вам данная команда не доступна')



