from aiogram import types

from loader import dp

from data.config import ADMINS

@dp.message_handler(commands='statistic')
async def statistic(message: types.Message):
    if f'{message.from_user.id}' in ADMINS:
        await message.answer('[Из базы] Все зарегистрированные пользователи')
    else:
        await message.answer('Вам дання команда не доступна')