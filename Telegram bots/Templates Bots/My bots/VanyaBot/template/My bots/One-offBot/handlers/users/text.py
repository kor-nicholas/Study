from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from loader import dp

from keyboards.default.menu import back, main, shop_markup, back_shop
from keyboards.inline.read import read, order_button

from aiogram.dispatcher import FSMContext
from states.state import Input

from sql.sql_db import SQL_product, SQL_shop, SQL_people
from data.config import db_sql

@dp.message_handler()
async def bot_echo(message: types.Message):
    if message.text == "Список товаров 🔽":

        # Достаем из базы весь товар
        sql_object = SQL_product(db_sql)
        products = sql_object.sql_select_all()
        sql_object.sql_close()

        # Сообщение с кнопкой Назад (в Главное меню)
        await message.answer("Список товаров, которые есть в наличии", reply_markup=back)

        # Перебираем все товары из базы и каждому товару создаем кнопки (в callback_data передаем id товара)
        for product in products:
            # product[0] - id ; product[1] - name ; product[2] - description ; product[3] - prise ; product[4] - photo_id ;
            #product[5] - count
            buy = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('-', callback_data=f'{product[0]}-1'),
                    InlineKeyboardButton('1', callback_data='count'),
                    InlineKeyboardButton('+', callback_data=f'{product[0]}+1')
                ],
                [
                    InlineKeyboardButton('Добавить в корзину', callback_data=f'{product[0]}|1')
                ]
            ])

            # Все еще в цикле выводим фотографию с даными о товаре
            await message.answer_photo(caption=f"Название: {product[1]}\n\nОписание: \n{product[2]}\n\nЦена: {product[3]}\n\nКоличество: {product[5]}", photo=product[4], reply_markup=buy)

    elif message.text == "Удалить из корзины по номеру":
        await message.answer("Введите номер товара, который хотите удалить", reply_markup=ReplyKeyboardRemove())
        await Input.delete.set()

    elif message.text == "Очистить корзину 🧹":

        # Удаляем все данные из базы по telegram_id человека
        sql_object = SQL_shop(db_sql)
        sql_object.sql_delete_all_for_telegram_id()
        sql_object.sql_close()

        # Удаляем сообщение со старой корзиной
        await message.delete()
        await message.chat.delete_message(message.message_id - 1)
        await message.answer("Корзина очищена", reply_markup=back_shop)

    elif message.text == "🔙 Назад":
        await message.answer(f"И снова здравствуй, {message.from_user.full_name}!\n"
                             f"Ну что ? Что-то выбрал ? Если нет, то можешь снова нажать на кнопку и выбрать 👇",
                             reply_markup=main)

    elif message.text == 'Информационный раздел ℹ':
        # Информационный раздел + кнопка "Я прочитал" (делает в базе '+', если уже есть '+', то кнопка не появляется)

        # Текст информационного раздела
        rules = "Вы зашли в информационный раздел"

        # Проверка в базе прочитал ли юзер правила
        sql_object = SQL_people(db_sql)
        read_info = sql_object.select_read_for_telegram_id(message.chat.id)
        sql_object.sql_close()

        # Если человек прочитал (read[0] == '+', то не выводим клавиатуру; если не прочитал - то добавляем кнопку чтобы прочитал)
        if read_info[0] == '-':
            await message.answer(rules, reply_markup=read)
        if read_info[0] == '+':
            await message.answer(rules, reply_markup=back)


    elif message.text == "Корзина 🛒" or "🔙 Вернуться в корзину":

        # Достаем из базы все товары которые находятся в корзине у пользователя
        sql_object = SQL_shop(db_sql)
        shops = sql_object.sql_select_all_for_telegram_id(message.chat.id)
        sql_object.sql_close()

        # Делаем переменную для общей суммы корзины
        total = 0

        # Готовим текст для корзины
        text_shop = "В корзине : \n\n"
        for shop in shops:
            # shop[0] - id ; shop[1] - telegram_id ; shop[2] - name ; shop[3] - prise ; shop[4] - count ; shop[5] - total
            text_shop += f"{shop[0]}. {shop[2]} x {shop[4]} = {shop[5]}грн\n"
            total += int(shop[5])
        text_shop += f"\nИтоговая сумма : {total}грн"

        # Добавляем в таблицу people общую сумму(total)
        sql_object = SQL_people(db_sql)
        sql_object.add_total_for_telegram_id(total, message.chat.id)
        sql_object.sql_close()

        # Отправляем текст корзины с кнопкой для работы с корзиной (Очистить, Удалить товар по id, Назад)
        await message.answer(text_shop, reply_markup=shop_markup)
        await message.answer("Для того чтобы оформить заказ, нажмите на кнопку Оплатить 👇", reply_markup=order_button)

@dp.message_handler(state=Input.delete)
async def delete_for_id_shop(message: types.Message, state: FSMContext):

    # Удаляем товар по id, который ввел пользователь
    sql_object = SQL_shop(db_sql)
    sql_object.sql_delete_for_id(message.text)
    sql_object.sql_close()

    await state.finish()

    # Удаления сообщения со старой корзиной
    await message.chat.delete_message(message.message_id - 3)
    await message.chat.delete_message(message.message_id - 2)
    await message.answer("Товар удален из корзины", reply_markup=back_shop)

