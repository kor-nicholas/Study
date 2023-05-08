from aiogram import types

from loader import dp

from data.config import ADMINS

@dp.message_handler(commands='help')
async def bot_help(message: types.Message):
    if f'{message.from_user.id}' in ADMINS:
                await message.answer('Список команд: \n' + 
                '/start - Начать диалог \n' + 
                '/help - Получить справку \n' + 
                '/statistic - Просмотреть статистику \n' + 
                '/broadcast - Сделать рассылку')
    else:
        await message.answer('Список команд: \n' + 
                '/start - Начать диалог \n' + 
                '/help - Получить справку \n')










