from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.test import buy
from keyboards.inline.test_inline import buy_1

from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    pass