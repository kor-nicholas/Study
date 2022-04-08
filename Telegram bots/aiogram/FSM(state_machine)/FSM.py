from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp
from states.test import Test # импортируем для работы с состояниями

@dp.message_handler(Command("test"), state=None)
async def enter_test(message : Message):
    await message.answer("Вы начали тестирование\nВопрос №1\nВведите електронную почту") # 1 вопрос
    await Test.Q1.set() # 1 ответ (получаем в состояние Q1)

@dp.message_handler(state=Test.Q1) # хендлер, который принимает ответ на 1 вопрос
async def answer_q1(message : Message, state : FSMContext):
    answer = message.text # ответ на 1 вопрос
    await state.update_data(answer1=answer) # сохраняем ответ на 1 вопрос
    await message.answer("Вопрос №2\nКупите товар по ссылке : url-link")
    await Test.next() # ждем ответ на 2 вопрос

@dp.message_handler(state=Test.Q2) # хенждер, который ловит ответ на 2 вопрос
async def answer_q2(message : Message, state : FSMContext):
    data = await state.get_data() # возвращает словарь, всего состояния (всех ответов)
    answer1 = data.get("answer1") # достаем из нашего  состояния ответ на 1 вопрос
    answer2 = message.text
    await message.answer("Спасибо за ответы, в скорем времени наш модератор с вами свяжеться и выплатит ваш бонус")
    await state.finish() # стираем состояние

#@dp.message_handler(state="*") # Любое состояние, все равно хендлер его выловит

# Порядок прописывания хендлеров имеет значение (все хендлеры работаюсь сверхну вниз)