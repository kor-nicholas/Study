import logging
import time

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states.states import GetInfoAboutUser

@dp.message_handler(state=GetInfoAboutUser.nick_name)
async def get_email(message: types.Message, state: FSMContext):
    nick_name = message.text

    await message.answer('Подождите, идет проверка никнейма ...')

    try:
        if message.from_user.username != nick_name:
            raise Exception('Nick_name isn\'t valid')

        await state.update_data(nick_name=str(nick_name))
        time.sleep(2)

        info = await state.get_data()
        await message.answer(f"(добавление данных в базу: \n\nEmail: {info['email']}\nPhone: {info['phone']}\nNick_name: {info['nick_name']})")
        await state.finish()

        await message.answer('Благодарим за подписку, как только выйдут новые игры на которых вы сможете заработать - мы вас уведомим')

    except Exception as ex:
        logging.error(ex)
        await message.answer('Укажите действительный никнейм / измените никнейм в настройках')
        time.sleep(2)








        

