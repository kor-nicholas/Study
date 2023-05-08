from loader import dp
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.inline.test_inline import buy_1,buy_2_1,buy_2_2,buy_visa_1,buy_visa_2
from keyboards.default.test import buy

@dp.callback_query_handler(text="month")
async def pear(call : CallbackQuery):
    await call.message.edit_text(text="Месяц\n"
                                      "Цена: 1200 руб.\n\n"
                                      "Срок подписки: 30 дней\n"
                                      "Вы получите приглашение в канал/чат 👇\n"
                                      "— Alknwt Private 🔞",reply_markup=buy_2_1)

@dp.callback_query_handler(text="year")
async def pear_2(call : CallbackQuery):
    await call.message.edit_text(text="Год\n"
                                      "Цена: 4000 руб.\n\n"
                                      "Срок подписки: 365 дней\n"
                                      "Вы получите приглашение в канал/чат 👇\n"
                                      "— Alknwt Private 🔞",reply_markup=buy_2_2)

@dp.callback_query_handler(text=['visa1','visa2'])
async def pear_4(call : CallbackQuery):
    if call.data == 'visa1':
        await call.message.edit_text(text="Способ оплаты: 💵 Visa/MasterCard\n"
                                          "Сумма к оплате: 1200 руб.\n"
                                          "Информация об оплате:\n"
                                          "Номер карты - 4890 4947 5404 9021\n"
                                          "__________________________\n"
                                          "Вы платите физическому лицу.\n"
                                          "Деньги поступят на счёт получателя.", reply_markup=buy_visa_1)
    elif call.data == 'visa2':
        await call.message.edit_text(text="Способ оплаты: 💵 Visa/MasterCard\n"
                                          "Сумма к оплате: 4000 руб.\n"
                                          "Информация об оплате:\n"
                                          "Номер карты - 4890 4947 5404 9021\n"
                                          "__________________________\n"
                                          "Вы платите физическому лицу.\n"
                                          "Деньги поступят на счёт получателя.", reply_markup=buy_visa_2)

@dp.callback_query_handler(text="back_main")
async def pear_5(call : CallbackQuery):
    await call.message.delete()
    await call.message.answer("Приветствующие сообщение от бота", reply_markup=buy)

#@dp.callback_query_handler(text=['purchase1','purchase2'])
#async def pear_6(call : CallbackQuery):
#    if call.data == 'purchase1':
#        pass
#    elif call.data == 'purxhase2':
#        pass

@dp.callback_query_handler(text=['check1','check2'])
async def pear_6(call : CallbackQuery):
    if call.data == 'check1':
        await call.answer("Проверка")
        await call.message.answer("Тут можно сделать проверку оплаты, но как она делается - я пока не знаю")
    elif call.data == 'check2':
        await call.answer("Проверка")
        await call.message.answer("Тут можно сделать проверку оплаты, но как она делается - я пока не знаю")

@dp.callback_query_handler(text=['back2_1_1','back2_1_2'])
async def pear_6(call : CallbackQuery):
    if call.data == 'back2_1_1':
        await call.message.edit_text(text="Месяц\n"
                                          "Цена: 1200 руб.\n\n"
                                          "Срок подписки: 30 дней\n"
                                          "Вы получите приглашение в канал/чат 👇\n"
                                          "— Alknwt Private 🔞", reply_markup=buy_2_1)
    elif call.data == "back2_1_2":
        await call.message.edit_text(text="Год\n"
                                          "Цена: 4000 руб.\n\n"
                                          "Срок подписки: 365 дней\n"
                                          "Вы получите приглашение в канал/чат 👇\n"
                                          "— Alknwt Private 🔞", reply_markup=buy_2_2)