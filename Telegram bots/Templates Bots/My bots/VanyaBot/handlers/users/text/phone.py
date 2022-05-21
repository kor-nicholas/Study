import logging
import phonenumbers
import time

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states.states import GetInfoAboutUser

@dp.message_handler(state=GetInfoAboutUser.phone)
async def get_email(message: types.Message, state: FSMContext):
    phone = message.text

    await message.answer('Подождите, идет проверка номера телефона ...')

    try:
        phone_number = phonenumbers.parse(phone)

        if phonenumbers.is_valid_number(phone_number) == False:
            raise Exception('Phone number isn\'t valid')

        await state.update_data(phone=str(phone))
        time.sleep(2)

        await message.answer('Введите ваш никнейм в Телеграм')
        await GetInfoAboutUser.nick_name.set()

    except Exception as ex:
        logging.error(ex)
        await message.answer('Укажите действительный номер телефона')
        time.sleep(2)








