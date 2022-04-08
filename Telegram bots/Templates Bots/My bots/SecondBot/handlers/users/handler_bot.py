from loader import dp
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from states.state import Test
from keyboards.reply.reply_keyboards import start_reply_mupkup, back, products
from private.config import group_id

@dp.message_handler(commands=['start'])
async def start(message : Message):
    await message.answer("Приветствие",reply_markup=start_reply_mupkup)

@dp.message_handler(content_types=['text'],state=None)
async def text(message : Message):
    if message.text == "Продукты":
        await message.answer("2-3 товара + ссылка на Амазон",reply_markup=back)
    elif message.text == "Назад":
        await message.answer("Приветствие",reply_markup=start_reply_mupkup)
    elif message.text == "Тест":
        await message.answer("1 вопрос",reply_markup=ReplyKeyboardRemove())
        await Test.Q1.set() # получаем ответ в состояние 1

@dp.message_handler(state=Test.Q1)
async def answer1(message : Message, state : FSMContext):
    answer = message.text # ответ на 1 вопрос
    await state.update_data(answer1=answer) # сохраняем ответ на 1 вопрос
    await message.answer("2 вопрос")
    await Test.next() # ждем ответ на 2 вопрос

@dp.message_handler(state=Test.Q2)
async def answer2(message : Message, state : FSMContext):
    answer = message.text # ответ на 2 вопрос
    await state.update_data(answer2=answer) # сохраняем ответ на 2 вопрос
    await message.answer("3 вопрос")
    await Test.next() # ждем ответ на 3 вопрос

@dp.message_handler(state=Test.Q3)
async def answer3(message : Message, state : FSMContext):
    answer = message.text # ответ на 3 вопрос
    await state.update_data(answer3=answer) # сохраняем ответ на 3 вопрос
    await message.answer("Введите почту")
    await Test.next() # ждем почту

@dp.message_handler(state=Test.Q4)
async def answer4(message : Message, state : FSMContext):
    email = message.text # почта
    await state.update_data(email=email) # сохраняем почту
    all_answers = await state.get_data() # словарь всех ответов
    await message.answer("В течении 24 часов мы на почту отправим бонус")
    await message.bot.send_message(group_id, f"Заявка от {message.from_user.first_name} (@{message.from_user.username})"
                                             f"\nОтвет на 1 вопрос : {all_answers['answer1']}\nОтвет на 2 вопрос : {all_answers['answer2']}"
                                             f"\nОтвет на 3 вопрос : {all_answers['answer3']}\nEmail : {all_answers['email']}")