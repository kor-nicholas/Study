# Работа с кнопками (прописывание хендлеров)
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.inline.keyboards import main_keyboard, pear_keyboard, apple_keyboard
from keyboards.reply.keyboards import menu

@dp.message_handler(Command("start"))
async def start(message : Message):
    await message.answer(("Главное меню"),reply_markup=menu)

@dp.callback_query_handler(text="pear") # Полностью совпадение callback
async def pear(call : CallbackQuery):
    #await call.answer(cache_time=60) # 60 секунд бот не будет получать апдейты
    await call.answer(f"call : {call.data}") # call.data -> pear; call.answer - уведомление в черном квадрате (на пару секунд)
    await call.message.answer("Вы выбрали грушу", reply_markup=pear_keyboard) # отвечает текстовым сообщением на кнопку

@dp.callback_query_handler(text="apple")
async def apple(call : CallbackQuery):
    await call.answer("Отличный выбор")
    await call.message.answer("Вы выбрали яблоко", reply_markup=apple_keyboard)

@dp.callback_query_handler(text="cancel")
async def cancel(call : CallbackQuery):
    await call.answer("Вы отменили покупку", show_alert=True) # show_alert - кнопка ОК в уведомлении
    await call.message.edit_reply_markup() # Удаление клавиатуры из под сообщения
    await call.message.answer("Главное меню", reply_markup=menu)

@dp.callback_query_handler(text_contains="pear") # Если в callback будет подстрока pear, то поймает этот хендлер
async def pear_2(message : Message):
    pass

@dp.message_handler(text=["Купить", "Продать"])
async def buy_or_purchase(message : Message):
    if message.text == "Купить":
        await message.answer("Выберите, что хотите купить", reply_markup=ReplyKeyboardRemove())
        await message.answer("У нас есть : 5 яблук, 1 груша",reply_markup=main_keyboard)
    if message.text == "Продать":
        await message.answer("Чтобы продать товар, нужно его купить :)",reply_markup=ReplyKeyboardRemove())
        await message.answer("Главное меню", reply_markup=menu)

@dp.message_handler(text="Назад")
async def back(message : Message):
    await message.answer("Главное меню", reply_markup=menu)