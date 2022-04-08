import telebot
from telebot import types

bot = telebot.TeleBot('1259568399:AAH9a-2E3LKyVHldr73wxuuObA404M53EvM')

# 1259568399:AAH9a-2E3LKyVHldr73wxuuObA404M53EvM - мой test_145_bot
# 1655844583:AAHiYQ6HBzVwRMDwccSxZp2bptPfeYZvpV4 - наш sales_test0q_bot

group_id = '-1001442909347' # Проверка ботов 2
group_id2 = '-1001468752097' # Проверка ботов 3
request_info = {}
nicks = []
nick = []
moder_id = []
id = {}


@bot.message_handler(commands=['start'])
def Start(message):
    nic = False
    for nick in nicks:
        if nick == message.from_user.username:
            nic = True
    if nic == False:
        nicks.append(message.from_user.username)
    id[f'{message.from_user.username}'] = f'{message.chat.id}'
    startmenu = types.ReplyKeyboardMarkup(True, True)
    startmenu.row('GO')
    bot.send_message(message.chat.id, 'Hello , I can make you a special offer. \nClick GO ', reply_markup=startmenu)
    bot.send_message(group_id2, 'Hello , I can make you a special offer. \nClick GO ', reply_markup=startmenu)


@bot.message_handler(commands=['send_text'])
def send_text(message):
    bot.send_message(message.chat.id, "Список всех ников пользователей : ")
    text_nicks = ''
    for nick in nicks:
        text_nicks += f"@{nick}\n"
    bot.send_message(message.chat.id, text_nicks + "\n\nВведите ник пользователя, кому хотите отправить сообщение : ")
    bot.register_next_step_handler(message, get_nick)


@bot.message_handler(commands=['reply'])
def reply(message):
    bot.send_message(message.chat.id, "Введите сообщение модератору : ")
    bot.register_next_step_handler(message, reply2)


@bot.message_handler(content_types=['text'])
def Zal(message):
    if message.text == 'GO':
        bot.send_message(message.chat.id,
                         ' You are just 2 steps away from getting your new Manual Juice and a Bonus $ Gift Normal Gift Card. \nEnter your name: ')
        bot.send_message(group_id2,
                         ' You are just 2 steps away from getting your new Manual Juice and a Bonus $ Gift Normal Gift Card. \nEnter your name: ')
        bot.register_next_step_handler(message, next2)

    elif message.text == 'I am ready':
        vibor1 = types.ReplyKeyboardMarkup(True, False)
        vibor1.row('⬅Back to')

        bot.send_message(message.chat.id,
                         'Buy our Product Name. \nSend us your Order number or the \nscreenshot of your purchase. \nUpon receipt of the parcel from Amazon  ',
                         reply_markup=vibor1)
        bot.send_message(group_id2,
                         'Buy our Product Name. \nSend us your Order number or the \nscreenshot of your purchase. \nUpon receipt of the parcel from Amazon  ',
                         reply_markup=vibor1)




    elif message.text == 'I am not interested':
        vibor3 = types.ReplyKeyboardMarkup(True, False)
        vibor3.row('⬅Back to')
        bot.send_message(message.chat.id, 'Set Product name to Liquid', reply_markup=vibor3)
        bot.send_message(group_id2, 'Set Product name to Liquid', reply_markup=vibor3)

    elif message.text == '⬅Back to':
        next2(message)


def get_nick(message):
    nick.append(message.text)
    bot.send_message(message.chat.id, "Введите сообщение, которое хотите отправить : ")
    bot.register_next_step_handler(message, send)


def send(message):
    moder_id.append(message.chat.id)
    bot.send_message(id[f'{nick[-1]}'], message.text)
    bot.send_message(id[f'{nick[-1]}'], "Если хотите ответить модератору, то введите команду /reply")


def reply2(message):
    bot.send_message(moder_id[-1], message.text)


def next2(message):
    vibor = types.ReplyKeyboardMarkup(True, False)
    vibor.row('I am ready')
    vibor.row('I am not interested')

    # Отправляем сообщение и отправляем подключение клавиатуры
    bot.send_message(message.chat.id,
                     "Dear🤝 " + message.from_user.first_name + ",how to get your free Gift Nominal Gift Card or 100% Refaund on Paypal: \n -Buy our Product \n-Send us your Order number photo \n-After receiving the parcel, leave a review",

                     reply_markup=vibor)
    bot.send_message(group_id2,
                     "Dear🤝 " + message.from_user.first_name + ",how to get your free Gift Nominal Gift Card or 100% Refaund on Paypal: \n -Buy our Product \n-Send us your Order number photo \n-After receiving the parcel, leave a review",

                     reply_markup=vibor)

    bot.register_next_step_handler(message, next3)


def next3(message):
    if message.text == 'I am ready':
        bot.send_message(message.chat.id, 'Sure i will')
        vibor1 = types.ReplyKeyboardMarkup(True, False)
        vibor1.row('Sure i will')
        bot.send_message(message.chat.id, 'Last question', reply_markup=vibor1)
        bot.send_message(group_id2, 'Last question', reply_markup=vibor1)
        bot.register_next_step_handler(message, next4)

    elif message.text == '⬅Back to':
        next2(message)


def next4(message):
    if message.text == 'Sure i will':
        vibor2 = types.ReplyKeyboardMarkup(True, False)
        vibor2.row('⬅Back to')
        bot.send_message(message.chat.id, 'Please send us your E-mail address')
        bot.send_message(message.chat.id, 'Last question', reply_markup=vibor2)
        bot.send_message(group_id2, 'Please send us your E-mail address')
        bot.send_message(group_id2, 'Last question', reply_markup=vibor2)

        bot.register_next_step_handler(message, input_email)
        bot.register_next_step_handler(message, next5)


def input_email(message):
    if '@' in message.text:
        request_info['mail'] = message.text


def next5(message):
    markup_inline = types.InlineKeyboardMarkup()

    item_link = types.InlineKeyboardButton(text='Juicers BONUS',
                                           url='https://mistresskitchen.com/collections/juicers/products/manual-juice-squeezer')

    markup_inline.add(item_link)
    bot.send_message(message.chat.id, 'Buy the product from the link', reply_markup=markup_inline)
    bot.send_message(group_id2, 'Buy the product from the link', reply_markup=markup_inline)

    markup_reply = types.ReplyKeyboardMarkup(True, True)
    markup_reply.row('I bought')

    bot.send_message(message.chat.id, 'If you bought a product, click the button below', reply_markup=markup_reply)
    bot.send_message(group_id2, 'If you bought a product, click the button below', reply_markup=markup_reply)

    bot.register_next_step_handler(message, next6)


def next6(message):
    if message.text == 'I bought':
        markup_inline = types.InlineKeyboardMarkup()
        item_yes = types.InlineKeyboardButton(text='I put 5 stars', callback_data='star')
        markup_inline.add(item_yes)
        bot.send_message(message.chat.id, 'After 3 days, please give 5 stars and review', reply_markup=markup_inline)
        bot.send_message(group_id2, 'After 3 days, please give 5 stars and review', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'star':
        markup_inline = types.InlineKeyboardMarkup()
        item_gift = types.InlineKeyboardButton(text='Gift Card', callback_data='gift')
        item_pay = types.InlineKeyboardButton(text='Pay Pal', callback_data='pay')
        markup_inline.add(item_gift, item_pay)
        bot.send_message(call.message.chat.id, 'Do you want 100% Refaund on Pay Pal or gift card ?',
                         reply_markup=markup_inline)
        bot.send_message(group_id2, 'Do you want 100% Refaund on Pay Pal or gift card ?', reply_markup=markup_inline)
    elif call.data == 'gift':
        request_info['choose'] = 'Gift Card'
        bot.send_message(call.message.chat.id, 'Send a screen about payment')
        bot.send_message(group_id2, 'Send a screen about payment')
    elif call.data == 'pay':
        request_info['choose'] = 'Pay Pal'
        bot.send_message(call.message.chat.id, 'Send a screen about payment')
        bot.send_message(group_id2, 'Send a screen about payment')


@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.chat.id, 'thank you, we will contact you within 24 hours')
    request_info['photo_id'] = message.photo[-1].file_id
    bot.send_message(group_id,
                     f"Заявка от {message.from_user.first_name}(@{message.from_user.username})\nEmail : {request_info['mail']}\nПлатежная система : {request_info['choose']}")  # Отправка заявки в группу модеров (request_info['email'] - почта пользователя)
    bot.send_photo(group_id, request_info['photo_id'])



bot.polling()