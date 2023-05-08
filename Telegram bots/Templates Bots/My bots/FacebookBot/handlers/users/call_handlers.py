from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from loader import dp

from sql.sql_db import SQL_product, SQL_shop, SQL_people
from data.config import db_sql

from data.config import ADMINS

from aiogram.dispatcher.storage import FSMContext

@dp.callback_query_handler()
async def all_callback(call: types.CallbackQuery):
    if '+' in call.data:
        index = call.data.find('+')
        id = call.data[:index]
        count = int(call.data[index + 1:])

        sql_object = SQL_product(db_sql)

        count_in_store = sql_object.sql_select_count_for_id(id) # count_in_store[0] - количество на складе

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
            ])) # !!! Изменение товаров !!!
        sql_object.sql_close()

    elif '-' in call.data:
        index = call.data.find('-')
        id = call.data[:index]
        count = -int(call.data[index + 1:])

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
        index = call.data.find('|')
        id = call.data[:index]
        count = int(call.data[index + 1:])

        sql_object = SQL_product(db_sql)
        sql_object2 = SQL_shop(db_sql)

        # info[0] - id ; info[1] - name ; info[2] - description ; info[3] - prise ; info[4] - photo_id ; info[5] - count
        info = sql_object.sql_select_for_id(id)

        sql_object.sql_close()

        total = count * info[3]

        sql_object2.sql_add(str(call.message.chat.id), info[1], info[3], count, total)
        await call.answer("Товар добавлен в корзину")

        sql_object2.sql_close()

    elif 'confirm' in call.data and call.data[-1] == '?':
        telegram_id = call.data[:call.data.find('confirm')]

        await call.answer("Подождите некоторое время, наш менеджер проверит оплату и подтвердит покупку")

        for admin in ADMINS:
            confirm = InlineKeyboardMarkup(inline_keyboard=[
                [
                    InlineKeyboardButton('Подтвердить оплату ✅', callback_data=f'{telegram_id}confirm='),
                    InlineKeyboardButton('Не оплачено ❌', callback_data=f'{telegram_id}confirm_')
                ]
            ])

            sql_object = SQL_shop(db_sql)

            shops = sql_object.sql_select_all_for_telegram_id(telegram_id)

            total = 0

            text_shop = f"У @{call.message.chat.username} в корзине : \n\n"
            for shop in shops:
                # shop[0] - id ; shop[1] - telegram_id ; shop[2] - name ; shop[3] - prise ; shop[4] - count ; shop[5] - total
                text_shop += f"{shop[0]}. {shop[2]} x {shop[4]} = {shop[5]}грн\n"
                total += int(shop[5])

            sql_object.sql_close()

            text_shop += f"\nИтоговая сумма : {total}грн"

            await call.message.bot.send_message(admin, text_shop)
            await call.message.bot.send_message(admin,
                                                f"@{call.message.chat.username} оплатил товар и ждет подтверждения ...",
                                                reply_markup=confirm)

    elif 'confirm' in call.data and call.data[-1] == '=':
        telegram_id = call.data[:call.data.find('confirm')]

        sql_object = SQL_people(db_sql)

        sql_object.change_file_id_to_pluss_for_telegram_id(telegram_id)

        sql_object.sql_close()

        for admin in ADMINS:
            await call.bot.send_message(admin, "Отправьте пожалуйста файл клиента: ")

    elif 'confirm' in call.data and call.data[-1] == '_':
        telegram_id = call.data[:call.data.find('confirm')]

        sql_object = SQL_people(db_sql)

        sql_object.change_file_id_to_minuss_for_telegram_id(telegram_id)

        sql_object.sql_close()

        await call.bot.send_message(telegram_id, "Оплатите пожалуйста товар")

    else:
        await call.answer("Это просто кнопка для отображения количества")

@dp.message_handler(content_types=['document'])
async def file(message: types.Message):
    sql_object = SQL_people(db_sql)

    telegram_id = sql_object.select_telegram_id_for_file_id("+")

    if len(telegram_id) == 1:
        await message.bot.send_message(telegram_id[0][0], "Товар оплачен, вот ваш заказ: ")
        await message.bot.send_document(telegram_id[0][0], message.document['file_id'])
    else:
        for admin in ADMINS:
            await message.bot.send_message(admin, "Слишком много людей, я не знаю кому отправлять файл")

    sql_object.change_file_id_to_minuss_for_telegram_id(telegram_id[0][0])
    sql_object.sql_close()

    sql_object = SQL_shop(db_sql)

    sql_object.sql_delete_all(telegram_id[0][0])
    sql_object.sql_close()
