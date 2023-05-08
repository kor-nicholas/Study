from time import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from loader import dp

from data.config import ADMINS

from sql.sql_db import SQL_product, SQL_shop, SQL_people
from data.config import db_sql

from keyboards.default.menu import back, get_product_buttons, confirm_button
from keyboards.inline.read import feedback

from states.state import Order

@dp.callback_query_handler()
async def all_callback(call: types.CallbackQuery):
    if '+' in call.data:

        # Распарсиваем всю инфу из callback_data
        index = call.data.find('+')
        id = call.data[:index]
        count = int(call.data[index:])

        # Достаем количество товара на складе (для того, чтобы человек не вышел за это число)
        sql_object = SQL_product(db_sql)
        count_in_store = sql_object.sql_select_count_for_id(id)
        sql_object.sql_close()

        # Если человек вышел за границу (больше чем есть товаров на складе), то предупреждение
        if count >= count_in_store[0]:
            await call.answer(f"На складе есть только {count_in_store[0]} товаров")
        else:
            await call.message.edit_reply_markup(InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('-', callback_data=f'{id}-{count + 1}'),
                    InlineKeyboardButton(f'{count + 1}', callback_data='count'),
                    InlineKeyboardButton('+', callback_data=f'{id}+{count + 1}')
                ],
                [
                    InlineKeyboardButton('Добавить в корзину', callback_data=f'{id}|{count + 1}')
                ]
            ]))

    elif '-' in call.data:

        # Распарсиваем всю инфу из callback_data
        index = call.data.find('-')
        id = call.data[:index]
        count = -int(call.data[index:])

        # Уведомляем человека, если он хочет меньше 1 товара заказать
        if count <= 1:
            await call.answer("Количество товаров не может быть меньше 1")
        else:
            await call.message.edit_reply_markup(InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('-', callback_data=f'{id}-{count - 1}'),
                    InlineKeyboardButton(f'{count - 1}', callback_data='count'),
                    InlineKeyboardButton('+', callback_data=f'{id}+{count - 1}')
                ],
                [
                    InlineKeyboardButton('Добавить в корзину', callback_data=f'{id}|{count - 1}')
                ]
            ]))

    elif '|' in call.data:

        # Распарсиваем всю инфу из callback_data
        index = call.data.find('|')
        id = call.data[:index]
        count = int(call.data[index + 1:])

        # Достаем всю информацию по товаре, на который кликнул человек (id товара передался по callback_data)
        sql_object = SQL_product(db_sql)
        # info[0] - id ; info[1] - name ; info[2] - description ; info[3] - prise ; info[4] - photo_id ; info[5] - count
        info = sql_object.sql_select_for_id(id)
        sql_object.sql_close()

        # Считаем общую стоимость за определенный товар, который выбрал человек
        total = count * info[3]

        # Добавляем его в базу Корзины
        sql_object2 = SQL_shop(db_sql)
        sql_object2.sql_add(str(call.message.chat.id), info[1], info[3], count, total)
        sql_object2.sql_close()

        await call.answer("Товар добавлен в корзину")

    elif call.data == 'read':

        # Меняем колонку read на +, то есть человек прочитал правила
        sql_object = SQL_people(db_sql)
        sql_object.change_read_for_telegram_id(call.message.chat.id)
        sql_object.sql_close()

        # Отправляем благодарственное сообщение + добавляем reply кнопку Назад
        await call.message.answer("Спасибо большое что прочитали этот раздел\n"
                                  "Для выхода в главное меню, нажмите на кнопку Назад 👇", reply_markup=back)

    elif 'order' in call.data:

        # Достаем из базы, прочитал ли пользователь Информационный раздел (правила, read: "+" или "-")
        sql_object = SQL_people(db_sql)
        read = sql_object.select_read_for_telegram_id(call.message.chat.id)
        sql_object.sql_close()

        if read[0] == '+':

            # Если человек прочитал Информационный раздел(FAQ) - оформление заявки (FSM)
            await call.message.answer("Оформление вашего заказа ... \n\nДля заказа, введите нужную информацию ... ", reply_markup=ReplyKeyboardRemove())
            await call.message.answer("Введите ваши ФИО: ")
            await Order.fio.set()

        elif read[0] == '-':

            # Если человек не прочитал Информационный раздел(FAQ) - просит прочитать
            await call.message.answer("Прочитайте пожалуйста Информационный раздел(FAQ), а потом продолжите оформление заявки", reply_markup=back)

        else:

            # Если в read ничего нету(но такого не должно случится вообще - ради подстраховки)
            print("Произошла ошибка None в столбце read (база: people)")

    else:

        # Если нажата кнопка на количество товаров
        await call.answer("Это просто кнопка для отображения количества")

@dp.message_handler(state=Order.fio)
async def input_fio(message: types.Message, state: FSMContext):

    # Сохраняем telegram_id и ФИО в Стейт
    await state.update_data(telegram_id=message.chat.id)
    await state.update_data(fio=message.text)

    # Просим телефон
    await message.answer("Введите пожалуйста ваш номер телефона: ")
    await Order.phone.set()

@dp.message_handler(state=Order.phone)
async def input_phone(message: types.Message, state: FSMContext):

    # Сохраняем в Стейт телефон
    await state.update_data(phone=message.text)

    # Просим город
    await message.answer("Введите ваш город: ")
    await Order.city.set()

@dp.message_handler(state=Order.city)
async def input_city(message: types.Message, state: FSMContext):

    # Сохраняем в Стейт город
    await state.update_data(city=message.text)

    # Просим выбрать способ доставки(почта или самовывоз)
    await message.answer("Выберите способ доставки", reply_markup=get_product_buttons)
    await Order.get_product.set()

@dp.message_handler(state=Order.get_product)
async def input_get_product(message: types.Message, state: FSMContext):

    # Сохраняем в Стейт способ доставки (почта или самовывоз)
    await state.update_data(get_product=message.text)

    if message.text == 'Почта 🚚':
        await message.answer("Введите номер отделение Новой почты: ", reply_markup=ReplyKeyboardRemove())
        await Order.post_office.set()
    elif message.text == 'Самовывоз 🚴‍♂️':
        await message.answer("Введите дату, когда вам будет удобнее всего встретиться", reply_markup=ReplyKeyboardRemove())
        await Order.date.set()
    else:
        await message.answer("Я не понял, что ты имеешь ввиду, выбери одну из кнопок 👇", reply_markup=get_product_buttons)
        await Order.get_product.set()

@dp.message_handler(state=Order.post_office)
async def input_place(message: types.Message, state: FSMContext):

    # Сохраняем в Стейт номер отделения Новой почты
    await state.update_data(post_office=message.text)
    info = await state.get_data()

    # Достаем total из таблицы people по telegram_id
    sql_object = SQL_people(db_sql)
    total = sql_object.select_total_for_telegram_id(message.chat.id)
    sql_object.sql_close()

    # Достаем информацию о Корзине по telegram_id
    sql_object = SQL_shop(db_sql)
    shop = sql_object.sql_select_all_for_telegram_id(message.chat.id)
    sql_object.sql_close()

    # total[0] - общая сумма
    # shop[0] - id в базе; shop[1] - telegram_id; shop[2] - name товара; shop[3] - цена; shop[4] - count; shop[5] - total(за товар)

    # Сообщение человеку, для подтверждения информации
    text = f"Ваша корзина:\n"
    for product in shop:
        text += f"{product[2]} : {product[3]} x {product[4]}шт = {product[5]}грн\n"
    text += f"\nИтоговая сумма: {total[0]}грн\n\n"

    # Информация о человеке
    text += f"Контактные данные:\nФИО: {info['fio']}\nТелефон: {info['phone']}\nГород: {info['city']}\n" \
             f"Способ доставки: {info['get_product']}\nНомер отделения Новой почты: {info['post_office']}"

    await message.answer(text)
    await message.answer("Перепроверьте информацию и подтвердите заказ 👇", reply_markup=confirm_button)
    await Order.confirm_send.set()


@dp.message_handler(state=Order.date)
async def input_data(message: types.Message, state: FSMContext):

    # Сохраняем в Стейт дату
    await state.update_data(date=message.text)

    # Просим время
    await message.answer("Введите время, когда вам будет удобнее всего встретиться")
    await Order.clock.set()

@dp.message_handler(state=Order.clock)
async def input_clock(message: types.Message, state: FSMContext):

    # Сохраняем в Стейт время
    await state.update_data(clock=message.text)
    info = await state.get_data()

    # Достаем total из таблицы people по telegram_id
    sql_object = SQL_people(db_sql)
    total = sql_object.select_total_for_telegram_id(message.chat.id)
    sql_object.sql_close()

    # Достаем информацию о Корзине по telegram_id
    sql_object = SQL_shop(db_sql)
    shop = sql_object.sql_select_all_for_telegram_id(message.chat.id)
    sql_object.sql_close()

    # total[0] - общая сумма
    # shop[0] - id в базе; shop[1] - telegram_id; shop[2] - name товара; shop[3] - цена; shop[4] - count; shop[5] - total(за товар)

    # Сообщение человеку, для подтверждения информации
    text = f"Ваша корзина:\n"
    for product in shop:
        text += f"{product[2]} : {product[3]} x {product[4]}шт = {product[5]}грн\n"
    text += f"\nИтоговая сумма: {total[0]}грн\n\n"

    # Информация о человеке
    text += f"Контактные данные:\nФИО: {info['fio']}\nТелефон: {info['phone']}\nГород: {info['city']}\n" \
            f"Способ доставки: {info['get_product']}\nДата: {info['date']}\nВремя: {info['clock']}"

    await message.answer(text)
    await message.answer("Перепроверьте информацию и подтвердите заказ 👇", reply_markup=confirm_button)
    await Order.confirm_send.set()

@dp.message_handler(state=Order.confirm_send)
async def input_confirm(message: types.Message, state: FSMContext):

    await state.update_data(confirm_send=message.text)

    if message.text == 'Подтвердить ✅':
        info = await state.get_data()

        # Достаем total из таблицы people по telegram_id
        sql_object = SQL_people(db_sql)
        total = sql_object.select_total_for_telegram_id(message.chat.id)
        sql_object.sql_close()

        # Достаем информацию о Корзине по telegram_id
        sql_object = SQL_shop(db_sql)
        shop = sql_object.sql_select_all_for_telegram_id(message.chat.id)
        sql_object.sql_close()

        # total[0] - общая сумма
        # shop[0] - id в базе; shop[1] - telegram_id; shop[2] - name товара; shop[3] - цена; shop[4] - count; shop[5] - total(за товар)

        # Сообщение - заказ админам:
        # Корзина
        order = f"Заказ от @{message.from_user.username}\n\nКорзина человека:\n"
        for product in shop:
            order += f"{product[2]} : {product[3]} x {product[4]}шт = {product[5]}грн\n"
        order += f"\nИтоговая сумма: {total[0]}грн\n\n"

        if info['get_product'] == 'Почта 🚚':

            # Информация о человеке
            order += f"Информация о человеке:\nФИО: {info['fio']}\nТелефон: {info['phone']}\nГород: {info['city']}\n" \
                     f"Способ доставки: {info['get_product']}\nНомер отделения Новой почты: {info['post_office']}"

        elif info['get_product'] == 'Самовывоз 🚴‍♂️':

            # Информация о человеке
            order += f"Информация о человеке:\nФИО: {info['fio']}\nТелефон: {info['phone']}\nГород: {info['city']}\n" \
                     f"Способ доставки: {info['get_product']}\nДата: {info['date']}\nВремя: {info['clock']}"

        # Отправка заявки админам
        for admin in ADMINS:
            await message.bot.send_message(admin, order)

        # Подтверждающее сообщение пользователю
        await message.answer("Ожидайте, ваш заказ, был отправлен менеджеру ... ", reply_markup=back)
        sleep(1)
        await message.answer("Если вам нужно связаться с ним, то нажмите на кнопку 👇", reply_markup=feedback)

        # Закрываем Стейт
        await state.finish()

        # Очистить корзину пользователя

    elif message.text == 'Переоформить заказ ❌':
        await message.answer("Переоформить заказ")





