from loader import dp
from aiogram.types import Message, CallbackQuery
from keyboards.inline.inline_keyboards import start_murkup, back_murkup, log_murkup

@dp.message_handler(commands=['start'])
async def start(message : Message):
    await message.answer("Главное меню",reply_markup=start_murkup)

@dp.callback_query_handler(text="profil") # кнопка Мой профиль
async def profil(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Ваш логин : @{call.message.chat.username}",reply_markup=back_murkup)

@dp.callback_query_handler(text="buy") # кнопка Покупка
async def buy(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите логи",reply_markup=log_murkup)

@dp.callback_query_handler(text="usa") # кнопка покупки логов USA в нопке Покупка
async def usa(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer("Логи USA")
    await call.message.answer("Кошелек для покупки")

@dp.callback_query_handler(text="mix") # кнопка покупки логов MIX в кнопке Покупка
async def mix(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer("Логи MIX")
    await call.message.answer("Кошелек для покупки")

@dp.callback_query_handler(text="rules") # кнопка Правила
async def rules(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer("Это правила",reply_markup=back_murkup)

@dp.callback_query_handler(text="back") # кнопка Назад
async def back(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer("Главное меню", reply_markup=start_murkup)