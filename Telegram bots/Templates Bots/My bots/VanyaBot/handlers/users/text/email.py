import logging
import time
from email_validator import validate_email, EmailNotValidError

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

from states.states import GetInfoAboutUser

@dp.message_handler(state=GetInfoAboutUser.email)
async def get_email(message: types.Message, state: FSMContext):
    email = message.text

    await message.answer('Подождите, идет проверка почты ...')

    try:
        emailObject = validate_email(email)

        email = emailObject.email

        await state.update_data(email=str(email))
        time.sleep(2)

        await message.answer('Введите ваш номер телефона (в международном формате: +380, +7, ...)')
        await GetInfoAboutUser.phone.set()

    except EmailNotValidError as emailError:
        logging.error(emailError)
        await message.answer('Укажите действительный адрес электронной почты')
        time.sleep(2)




        

