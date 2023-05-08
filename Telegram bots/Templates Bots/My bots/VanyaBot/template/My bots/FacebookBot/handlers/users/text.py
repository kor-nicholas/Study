from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from loader import dp

from aiogram.dispatcher import FSMContext
from states.state import Input

from keyboards.default.menu import back, main, shop_markup, back_shop

from sql.sql_db import SQL_product, SQL_shop
from data.config import db_sql

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "Список товаров 🔽":
        sql_object = SQL_product(db_sql)
        await message.answer("Список товаров, которые есть в наличии", reply_markup=back)
        for product in sql_object.sql_select_all():
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

            await message.answer_photo(caption=f"Название: {product[1]}\n\nОписание: \n{product[2]}\n\nЦена: {product[3]}\n\nКоличество: {product[5]}", photo=product[4], reply_markup=buy)
        sql_object.sql_close()

    elif message.text == "Удалить из корзины по номеру":
        await message.answer("Введите номер товара, который хотите удалить", reply_markup=ReplyKeyboardRemove())
        await Input.delete.set()

    elif message.text == "Очистить корзину 🧹":
        sql_object = SQL_shop(db_sql)

        sql_object.sql_delete_all(message.chat.id)
        sql_object.sql_close()

        await message.delete()
        await message.chat.delete_message(message.message_id - 1)
        await message.answer("Корзина очищена", reply_markup=back_shop)

    elif message.text == "🔙 Назад":
        await message.answer(f"И снова здравствуй, {message.from_user.full_name}!\n"
                             f"Ну что ? Что-то выбрал ? Если нет, то можешь снова нажать на кнопку и выбрать 👇",
                             reply_markup=main)

    elif message.text == "Корзина 🛒" or "🔙 Вернуться в корзину":
        sql_object = SQL_shop(db_sql)

        shops = sql_object.sql_select_all_for_telegram_id(message.chat.id)

        total = 0

        text_shop = "В корзине : \n\n"
        for shop in shops:
            # shop[0] - id ; shop[1] - telegram_id ; shop[2] - name ; shop[3] - prise ; shop[4] - count ; shop[5] - total
            text_shop += f"{shop[0]}. {shop[2]} x {shop[4]} = {shop[5]}грн\n"
            total += int(shop[5])

        sql_object.sql_close()

        text_shop += f"\nИтоговая сумма : {total}грн"
        await message.answer(text_shop, reply_markup=shop_markup)

        button_buy_link = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton("Оплатить", url="privatbank.com", callback_data=f"{message.chat.id}link")
            ]
        ])
        await message.answer("Для оплаты, нажмите на кнопку Оплатить 👇", reply_markup=button_buy_link)

        confirm = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton('Я оплатил ✅', callback_data=f'{message.chat.id}confirm?')
            ]
        ])
        await message.answer("После оплаты, нажмите на кнопку Я оплатил 👇", reply_markup=confirm)

@dp.message_handler(state=Input.delete)
async def delete_for_id_shop(message: types.Message, state: FSMContext):
    sql_object = SQL_shop(db_sql)

    print(f"{message.text} | {message.chat.id}")
    sql_object.sql_delete_for_id(message.text, message.chat.id) #id который ввел человек для удаления товара по id
    sql_object.sql_close()

    await state.finish()

    await message.chat.delete_message(message.message_id - 3)
    await message.chat.delete_message(message.message_id - 2)
    await message.answer("Товар удален из корзины", reply_markup=back_shop)

