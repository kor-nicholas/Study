from cgitb import text
import email
import logging
from aiogram import types

from loader import dp

from states.states import GetInfoAboutUser

from data.config import GROUP_ID

@dp.callback_query_handler(text='check_subcscribe')
async def check_subscribe(call: types.CallbackQuery):
    corutine_status = await call.bot.get_chat_member(chat_id=GROUP_ID, user_id=call.from_user.id)

    if corutine_status['status'] == 'member' or corutine_status['status'] == 'administrator' and corutine_status['status'] != 'left':
        await call.message.answer('Чтобы подписаться на рассылку - введите свой email')
        await GetInfoAboutUser.email.set()
    else:
        await call.answer('Подпишитесь пожалуйста на канал и приходите еще раз')

    



