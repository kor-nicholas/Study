from loader import dp
from time import sleep
from random import randint

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from keyboards.inline.inline_keyboards import category, manager, products, send_order, back_inline
from keyboards.reply.reply_keyboards import main, back_reply

from sql.sql_db import SQL_work
from config import db_sql, group_id

sql_object = SQL_work(db_sql)

from state.state import Add, Delete, Order, Find_code

@dp.message_handler(commands=['start'])
async def start(message : Message):
    await message.answer("Вiтання",reply_markup=main)

@dp.message_handler(commands=['group_id'])
async def group(message : Message):
    await message.answer(f"{message.chat.id}")

@dp.message_handler(commands=['comm_for_admin'])
async def comm_for_admin(message : Message):
    await message.answer("Всi адмiн. команди : \n/group_id - для того, щоб дiзнатись group_id группи, в яку будуть надсилатись заявки.\n"
                         "Спочатку потрiбно додати бота до группи, та ввести команду (потiм цей group_id, записати в config файл)\n"
                         "Також потрiбно в config файл потрiбно додати username менеджера"
                         "/add_product - додати товар до бота (по-етапно бот запросить iнформацiю)\n"
                         "/delete_product - видалити товар (запросить назву та цiну товара)\n"
                         "/all_product - переглянути всi товари, якi присутнi в ботi\n"
                         "/find_code - знайти товар по його коду продукту\n")

@dp.message_handler(commands=['find_code'])
async def find_code(message : Message):
    await message.answer("Введiть код продукту")
    await Find_code.code.set()

@dp.message_handler(state=Find_code.code)
async def code(message : Message, state : FSMContext):
    code_text = message.text
    await state.finish()
    info = sql_object.sql_select_for_code(code_text).fetchone()
    await message.answer_photo(
        caption=f"Назва : {info[0]}\n\nОпис : {info[2]}\n\nКод продукту : {info[5]}\n\nЦiна : {info[3]}",
        photo=info[4],
        reply_markup=back_inline)
    sleep(randint(0, 1))

@dp.message_handler(commands=['all_product'])
async def all_product(message : Message):
    info = sql_object.sql_select_all()
    await message.answer("Всi товари : \n")
    for i in info:
        await message.answer(f"Назва : {i[0]}\nКатегорiя : {i[1]}\nОпис : {i[2]}\nЦiна : {i[3]}\nPhoto_id = {i[4]}\nКод продукту = {i[5]}")

@dp.message_handler(commands=['add_product'])
async def add_product(message : Message, state : FSMContext):
    await message.answer("Введiть назву товару")
    await Add.name.set()

@dp.message_handler(state=Add.name)
async def add_name(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    await message.answer("Введiть категорiю товару (Телефон, Навушники, Часи, Камери, Iншi)")
    await Add.category.set()

@dp.message_handler(state=Add.category)
async def add_category(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(category=answer)
    await message.answer("Введiть опис товару")
    await Add.description.set()

@dp.message_handler(state=Add.description)
async def add_description(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(description=answer)
    await message.answer("Вiдправте фотографiю товару")

@dp.message_handler(content_types=['photo'], state='*')
async def photo(message : Message, state : FSMContext):
    answer = message.photo[-1].file_id
    await Add.photo_id.set()
    await state.update_data(photo_id=answer)
    await message.answer("Введiть код продукту")
    await Add.code.set()

@dp.message_handler(state=Add.code)
async def input_code(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(code=answer)
    await message.answer("Введiть цiну товару")
    await Add.prise.set()

@dp.message_handler(state=Add.prise)
async def add_prise(message : Message, state : FSMContext):
    answer = int(message.text)
    await state.update_data(prise=answer)
    info = await state.get_data()
    print(info)
    try:
        sql_object.sql_add_product(info['name'], info['category'], info['description'], info['prise'], info['photo_id'], info['code'])
    except:
        await message.answer("Помилка додавання данних до бази")
    await message.answer("Данi додано до бази данних")
    await state.finish()

@dp.message_handler(commands=['delete_product'])
async def delete_product(message : Message, state : FSMContext):
    await message.answer("Введiть назву товару")
    await Delete.name.set()

@dp.message_handler(state=Delete.name)
async def delete_name(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    await message.answer("Введiть цiну товару")
    await Delete.prise.set()

@dp.message_handler(state=Delete.prise)
async def delete_prise(message : Message, state : FSMContext):
    answer = int(message.text)
    await state.update_data(prise=answer)
    info = await state.get_data()
    try:
        sql_object.sql_delete_product(info['name'], info['prise'])
    except:
        await message.answer("Данi не знайдено")
    await message.answer("Данi видалено з бази данних")
    await state.finish()

@dp.message_handler()
async def text(message : Message):
    if message.text == 'Про магазин':
        await message.answer("Магзин мобільних пристроїв, аксесуарів пропонує великий вібір телефонів Xiaomi, Samsung, Huawei, оригінальні аксесуари Xiaomi, Bausen, Nillkin, Hoco, XO, Konfulon. \nНоутбуки нові і Б/У, а також пропонує якісний ремонт електроніки, з гарантією",reply_markup=back_reply)
    elif message.text == 'Контакти':
        await message.answer("Адресса : Б.Хмельницького 12, 79000 Львів\n\nНомера телефону :  \n0632714334\n0683714334\n\nВеб-сайт : https://mobile-phone-repair-shop-2731.business.site", reply_markup=back_reply)
    elif message.text == 'Список товару':
        await message.answer("Виберiть категорiю", reply_markup=category)
    elif message.text == 'Пiдтримка':
        await message.answer("Ви можете звернутись до нашого менеджера, для вияснення питань", reply_markup=manager)
    elif message.text == 'Бонуси (скидки)':
        await message.answer("Якщо присутнi бонуси, то можна додати сюди", reply_markup=back_reply)
    elif message.text == 'Назад':
        await message.answer("Вiтання", reply_markup=main)

@dp.callback_query_handler(text='phone')
async def phone(call : CallbackQuery):
    await call.message.delete()
    objects = sql_object.sql_select_for_category("Телефон")
    # 0 - назва; 1 - категорiя; 2 - опис; 3 - цiна; 4 - photo_id; 5 - код продукту
    await call.message.answer("Для того щоб замовити, натиснiть на кнопку", reply_markup=back_reply)
    for object in objects:
        await call.message.answer_photo(
            caption=f"Назва : {object[0]}\n\nОпис : {object[2]}\n\nКод продукту : {object[5]}\n\nЦiна : {object[3]}",
            photo=object[4],
            reply_markup=products)
        sleep(randint(0, 1))

@dp.callback_query_handler(text='headphones')
async def headphone(call : CallbackQuery):
    await call.message.delete()
    objects = sql_object.sql_select_for_category("Навушники")
    await call.message.answer("Для того щоб замовити, натиснiть на кнопку", reply_markup=back_reply)
    for object in objects:
        await call.message.answer_photo(
            caption=f"Назва : {object[0]}\n\nОпис : {object[2]}\n\nКод продукту : {object[5]}\n\nЦiна : {object[3]}",
            photo=object[4],
            reply_markup=products)
        sleep(randint(0, 1))

@dp.callback_query_handler(text='clock')
async def clock(call : CallbackQuery):
    await call.message.delete()
    objects = sql_object.sql_select_for_category("Часи")
    await call.message.answer("Для того щоб замовити, натиснiть на кнопку", reply_markup=back_reply)
    for object in objects:
        await call.message.answer_photo(
            caption=f"Назва : {object[0]}\n\nОпис : {object[2]}\n\nКод продукту : {object[5]}\n\nЦiна : {object[3]}",
            photo=object[4],
            reply_markup=products)
        sleep(randint(0, 1))

@dp.callback_query_handler(text='cameras')
async def camera(call : CallbackQuery):
    await call.message.delete()
    objects = sql_object.sql_select_for_category("Камери")
    await call.message.answer("Для того щоб замовити, натиснiть на кнопку", reply_markup=back_reply)
    for object in objects:
        await call.message.answer_photo(
            caption=f"Назва : {object[0]}\n\nОпис : {object[2]}\n\nКод продукту : {object[5]}\n\nЦiна : {object[3]}",
            photo=object[4],
            reply_markup=products)
        sleep(randint(0, 1))

@dp.callback_query_handler(text='other')
async def other(call : CallbackQuery):
    await call.message.delete()
    objects = sql_object.sql_select_for_category("Iншi")
    await call.message.answer("Для того щоб замовити, натиснiть на кнопку", reply_markup=back_reply)
    for object in objects:
        await call.message.answer_photo(
            caption=f"Назва : {object[0]}\n\nОпис : {object[2]}\n\nКод продукту : {object[5]}\n\nЦiна : {object[3]}",
            photo=object[4],
            reply_markup=products)
        sleep(randint(0, 1))

@dp.callback_query_handler(text='buy')
async def center(call : CallbackQuery, state : FSMContext):
    await Order.order_username.set()
    await state.update_data(username=call.message.chat.username)
    await call.message.answer("Введiть код продукту товару")
    await Order.order_code.set()

@dp.message_handler(state=Order.order_code)
async def code(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(code=answer)
    await message.answer("Введiть ваше iм'я")
    await Order.order_name.set()

@dp.message_handler(state=Order.order_name)
async def name(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    await message.answer("Введiть ваше прiзвище")
    await Order.order_first_name.set()

@dp.message_handler(state=Order.order_first_name)
async def first_name(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(first_name=answer)
    await message.answer("Введiть вашу краiну")
    await Order.order_country.set()

@dp.message_handler(state=Order.order_country)
async def country(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(country=answer)
    await message.answer("Введiть ваше мiсто")
    await Order.order_city.set()

@dp.message_handler(state=Order.order_city)
async def city(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(city=answer)
    await message.answer("Введiть ваше почтове вiддiлення")
    await Order.order_post.set()

@dp.message_handler(state=Order.order_post)
async def post(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(post=answer)
    await message.answer("Введiть ваш номер телефону")
    await Order.order_phone.set()

@dp.message_handler(state=Order.order_phone)
async def phone(message : Message, state : FSMContext):
    answer = message.text
    await state.update_data(phone=answer)
    await message.answer("Натиснiть на кнопку, для вiдправлення вашоi заявки", reply_markup=send_order)

@dp.callback_query_handler(text='send', state='*')
async def yes(call : CallbackQuery, state : FSMContext):
    info = await state.get_data()
    await state.finish()

    order = f"Заявка вiд : {info['name']} {info['first_name']} (@{info['username']})\nКраiна/мiсто : {info['country']}/{info['city']}\nПоштове вiддiлення : {info['post']}\nТелефон : {info['phone']}"

    await call.bot.send_message(group_id, order)
    await call.answer(
        "Дякуемо за замовлення. Ваша заявка вiдправлена модератору. Найближчим часов з вами зв'яжуться для уточнення всiх деталей замовлення", show_alert=True)

@dp.callback_query_handler(text=['back','main_menu'])
async def back(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer("Вiтання", reply_markup=main)