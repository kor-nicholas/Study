from loader import dp

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from keyboards.inline.inline_keyboards import *
from keyboards.reply.reply_keyboards import *

from config import photo_id

from state.state import Test

@dp.message_handler(commands=['start'])
async def start(message : Message):
    await message.answer(f"Привет {message.from_user.first_name}.\nЯ Капитан Робот-Доставки, рожден\nспасать жителей"
                         f"города от голода. С\nэтого момента, знай, я всегда готов тебе\nпомочь.\nНачнем?",reply_markup=main)

@dp.message_handler()
async def process_text(message : Message):
    if message.text == 'Новый заказ 🍽':
        await message.answer("Выберите тип заказа",reply_markup=type_order)
    elif message.text == 'Связаться с оператором 📞':
        await message.answer("+7 987 181-89-01")
    elif message.text == 'Акции и скидки 🎉':
        await message.answer("К сожалению, на данный момент акций и скидок нет.")
    elif message.text == 'Корзина 🛒':
        pass
    elif message.text == 'Назад':
        await message.delete()
        await message.answer_photo(caption='Меню', reply_markup=menu, photo=photo_id['main_menu'])

@dp.callback_query_handler(text='type_order')
async def type(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer("Доставка")
    await call.message.answer("Введите полный адрес")
    await Test.addres.set()

@dp.message_handler(state=Test.addres)
async def addres(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(addres=answer)
    await state.finish()
    await message.answer("Хотите ли вы, написать дополнительную информацию для курьера ?", reply_markup=yes_or_no)
    #await Test.more_info.set()

@dp.callback_query_handler(text='yes')
async def yes_(call : CallbackQuery):
    await call.answer("Введите сообщение")
    await call.message.delete()
    await Test.more_info.set()

@dp.message_handler(state=Test.more_info)
async def more_info(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(more_info=answer)
    await state.finish()
    await message.answer("Перейдем к меню ?",reply_markup=to_menu)

@dp.callback_query_handler(text='no')
async def no_(call : CallbackQuery, state : FSMContext):
    answer = call.message.text
    await state.update_data(more_info=answer)
    await state.finish()
    await call.message.delete()
    await call.message.answer("Перейдем к меню ?",reply_markup=to_menu)

@dp.callback_query_handler(text='menu')
async def menu_main(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption='Меню',reply_markup=menu,photo=photo_id['main_menu'])

@dp.callback_query_handler(text='bakery')
async def backary(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption='Меню',reply_markup=bakerys,photo=photo_id['main_menu'])

@dp.callback_query_handler(text='backery_1')
async def backary_1(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption='Булочки', reply_markup=bakerys_1, photo=photo_id['backery'])

@dp.callback_query_handler(text='garnish')
async def garnish(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption='Меню', reply_markup=garnishs, photo=photo_id['main_menu'])

@dp.callback_query_handler(text='garnish_1')
async def garnish_1(call : CallbackQuery):
    await call.message.delete()
    await call.message.delete()
    await call.message.answer_photo(
        caption='Креветки, мидии, кальмар, осьминог, особый бульон, томаты черри, '
                'сок лайма, сливки, рыбный соус и рис', reply_markup=garnishs_1, photo=photo_id['garnish'])

@dp.callback_query_handler(text='hot_meat')
async def hot_meat(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption='Меню', reply_markup=hot_meats, photo=photo_id['main_menu'])

@dp.callback_query_handler(text='hot_meat_1')
async def hot_meat_1(call : CallbackQuery):
    await call.message.delete()
    await call.message.delete()
    await call.message.answer_photo(
        caption='Мы подготовили специально для Вас вкусненькое предложение - курочку из элитного района Сеула - Gangnam. '
                'Рецептура отшлифованная годами завоевала Корею и весь мир своим неповторимым вкусом. '
                'Неудивительно что в большинстве стран Азии это является самым распространённым бизнес-ланчем',
        reply_markup=hot_meats_1, photo=photo_id['hot_meat'])

@dp.callback_query_handler(text='drink')
async def drink(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption='Меню', reply_markup=drinks, photo=photo_id['main_menu'])

@dp.callback_query_handler(text='drink_1')
async def drink_1(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        caption='Большой чикен — это "сборная" курочка в любом из 7-ми уникальных вкусов. '
                'В одном заказе вы получите крылышки, ножки, грудку и куриное филе. '
                'Это так легко ,но только вкусно и сытно 😋', reply_markup=drinks_1, photo=photo_id['drink'])

@dp.callback_query_handler(text='salat')
async def salat(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption='Меню', reply_markup=salats, photo=photo_id['main_menu'])

@dp.callback_query_handler(text='salat_1')
async def salat_1(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        caption='Как раз из таких.😊 \nЕго приятный,сладковатый вкус и необычное сочетание ингредиентов.'
                'Добавляют на вашу гастрономическую карту новый, интересный объект 🍲😌', reply_markup=salats_1, photo=photo_id['salat'])

@dp.callback_query_handler(text='cold_eat')
async def cold_eat(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption='Меню', reply_markup=cold_eats, photo=photo_id['main_menu'])

@dp.callback_query_handler(text='cold_eat_1')
async def cold_eat_1(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        caption='Онигири - — это традиционное японское блюдо, которое состоит из трех элементов: '
                'рис, начинка и лист прессованных водорослей. Такие японские сэндвичи отлично подойдут '
                'для правильного перекуса', reply_markup=cold_eats_1, photo=photo_id['cold_eat'])

@dp.callback_query_handler(text='-')
async def minus(call : CallbackQuery):
    await call.message.delete()
    a = change_a(a)
    await call.message.answer_photo(caption='Булочки', reply_markup=bakerys_1, photo=photo_id['backery'])

@dp.callback_query_handler(text='+')
async def plus(call : CallbackQuery, a = 1, b = 1, c = 1, d = 1, e = 1, f = 1):
    await call.message.delete()
    a += 1
    await call.message.edit_reply_markup()
    await call.message.answer_photo(caption='Булочки', reply_markup=bakerys_1, photo=photo_id['backery'])

@dp.callback_query_handler(text='back')
async def back(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(caption='Меню', reply_markup=menu, photo=photo_id['main_menu'])









@dp.message_handler(content_types=['photo'])
async def photo(message : Message):
    await message.answer(message.photo[-1].file_id)
    await message.answer(message.from_user.id)