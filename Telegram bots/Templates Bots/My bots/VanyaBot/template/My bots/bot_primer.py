## -*- coding: utf-8 -*-
import telebot
from telebot import types # кнопки
import smtplib # отправка на почту

# 1259568399:AAH9a-2E3LKyVHldr73wxuuObA404M53EvM - test_145_bot

bot = telebot.TeleBot('1119755573:AAGqWzU-sBh50yKYo3KSDrEpQciwgDsmCw8')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет,я бот который наконец-то поможет тебе заработать денег в интернете удаленно 😱 ')
    bot.send_message(message.chat.id, 'Чтобы просмотреть список всех команд,введи команду /commands')
    murkup_inline = types.InlineKeyboardMarkup() # создаем кавиатуру под сообщением

    button_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'yes') # создаем кнопку
    button_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'no') # создаем кнопку

    murkup_inline.add(button_yes, button_no) # добавляем в клавиатуру кнопки
    bot.send_message(message.chat.id, 'Но для начала,нам нужно твое соглашение на получение от нас писем. Ты готов получать все самые новые виды зароботка на почту ?', reply_markup = murkup_inline)

@bot.message_handler(commands=['commands'])
def commands(message):
    bot.send_message(message.chat.id, 'Список всех команд : ')
    bot.send_message(message.chat.id, '/statistic -> сколько времени осталось до начала рассылки')
    bot.send_message(message.chat.id, '/earn_money -> другие виды заработка')
    bot.send_message(message.chat.id, '/commands -> список всех команд бота')

statistic_num = 993

@bot.message_handler(commands=['statistic'])
def statistic(message):
    bot.send_message(message.chat.id, f'До начала рассылки осталось : {statistic_num}/1000 email-адресов в базе')

@bot.message_handler(commands=['earn_money'])
def earn_money(message):
    murkup_reply_earn = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button_bux = types.KeyboardButton('Буксы')
    button_nakrutka = types.KeyboardButton('Накрутка')
    button_cupon = types.KeyboardButton('Купоны')
    button_school = types.KeyboardButton('Школа')
    button_game = types.KeyboardButton('Игры')
    murkup_reply_earn.add(button_bux, button_nakrutka, button_cupon, button_school, button_game)
    bot.send_message(message.chat.id, 'Выберите категорию', reply_markup = murkup_reply_earn)

@bot.callback_query_handler(func = lambda call : True)
def inline_keyboard(call):
    if call.data == 'yes':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True) # создаем клавиатуру

        button_reg = types.KeyboardButton('Регистрация') # создаем кнопку

        murkup_reply.add(button_reg) # Добавляем в клавиатуру кнопку
        bot.send_message(call.message.chat.id, 'Отлично,теперь вам нужно зарегистрироваться. Для этого нажмите на кнопочку "Регистрация" и получите все знания 👇',reply_markup = murkup_reply)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Очень жаль что вам это не интересно 😭')

    elif call.data == 'bux_1':
        link_bux_1 = 'http://catcut.net/N4dM' # Seosprint
        bot.send_message(call.message.chat.id, f'Уни­каль­ное ме­сто! Оно объ­еди­ня­ет са­мых раз­ных и ин­те­рес­ных лю­дей. Раз­ни­ца в воз­расте, об­ра­зо­ва­нии, уровне до­стат­ка, на­цио­наль­но­сти и цве­те ко­жи здесь не име­ет ни­ка­ко­го зна­че­ния. Здесь мож­но ра­до­вать­ся эле­мен­тар­ным ме­ло­чам или ре­а­ли­зо­вы­вать ам­би­ци­оз­ные пла­ны. Это ме­сто, ко­то­рое раз­ви­ва­ет­ся его участ­ни­ка­ми. При­со­еди­няй­ся! Раз­ви­вай­ся, за­ра­ба­ты­вай, на­хо­ди дру­зей, со­зда­вай своё со­об­ще­ство! Переходи по ссылке -> {link_bux_1}')
    elif call.data == 'bux_2':
        link_bux_2 = 'http://catcut.net/Q4dM' # Advego
        bot.send_message(call.message.chat.id, f'Заработок на копирайтинге и переводе текстов — заказы на различные тематики для новичков и профи. Стабильный доход — в Адвего всегда есть работа: в будние дни, в выходные и даже ночью. Свободный график — разовые работы, частичная занятость, полный рабочий день. Переходи оп ссыле и зарабатывай -> {link_bux_2}')
    elif call.data == 'bux_3':
        link_bux_3 = 'http://catcut.net/15dM' # Socpublick
        bot.send_message(call.message.chat.id, f'ЗАРАБАТЫВАЙТЕ В ИНТЕРНЕТЕ! ДЕНЬГИ ЗА ВСЁ, ЧТО ВЫ РАНЬШЕ ДЕЛАЛИ БЕСПЛАТНО! Вас ждут тысячи заданий (небольших поручений рекламодателей) на любой вкус и цвет, делайте всё, что и раньше, на любимых сайтах и в соц. сетях, но теперь ещё и за деньги! Переходи по ссылке и зарабатывай -> {link_bux_3}')
    elif call.data == 'bux_4':
        link_bux_4 = 'http://catcut.net/55dM' # Taskpay
        bot.send_message(call.message.chat.id, f'Биржа заработка в Интернете на простых заданиях. Тысячи легких заданий с оплатой за деньги. Переходи по ссылке и зарабатывай -> {link_bux_4}')
    elif call.data == 'bux_5':
        link_bux_5 = 'http://catcut.net/75dM' # Wmrfast
        bot.send_message(call.message.chat.id, f'Мы предлагаем несколько видов заработка: 1. Просмотр рекламы - самый простой способ заработка 2. Выполнение заданий - самый прибыльный способ заработка. Переходи по ссылке и зарабатывай -> {link_bux_5}')

    elif call.data == 'nakrutka_1':
        link_nakrutka_1 = 'http://catcut.net/U4dM' # Bestliker
        bot.send_message(call.message.chat.id, f'Зарабатывайте монеты с помощью своих соц.сетей и потом сможете их обменять на деньги или на рекламу. Переходи по ссылке и зарабатывай (или рекламируйся) -> {link_nakrutka_1}')
    elif call.data == 'nakrutka_2':
        link_nakrutka_2 = 'http://catcut.net/n5dM' # Bosslike
        bot.send_message(call.message.chat.id, f'Зарабатывайте монеты с помощью своих соц.сетей и потом сможете их обменять на деньги или на рекламу. Переходи по ссылке и зарабатывай (или рекламируйся) -> {link_nakrutka_2}')
    elif call.data == 'nakrutka_3':
        link_nakrutka_3 = 'http://catcut.net/18dM' # LikeInsta
        bot.send_message(call.message.chat.id, f'Зарабатывайте монеты с помощью своих соц.сетей и потом сможете их обменять на деньги или на рекламу. Переходи по ссылке и зарабатывай (или рекламируйся) -> {link_nakrutka_3}')

    elif call.data == 'cupon_1':
        link_cupon_1 = 'http://catcut.net/GodM' # BonusMall
        bot.send_message(call.message.chat.id, f'Покупаете ставки -> Находите интересный товар -> Делаете ставку -> Запускается таймер -> Если за 20 секунд никто больше не сделал ставку - вы победитель! -> Покупаете товар за аукционную стоимость. Переходите по ссылке и покупайте товар по дешевке -> {link_cupon_1}')
    elif call.data == 'cupon_2':
        link_cupon_2 = 'http://catcut.net/sodM' # КупиКупон
        bot.send_message(call.message.chat.id, f'Боитесь позволить себе лишнее и часто отказываетесь от дружеских посиделок, вспоминая о толщине своего кошелька? Или располагаете средствами, но порой не знаете, как потратить их с удовольствием? А может быть, вы просто с азартом высматриваете новые акции, вне зависимости от того, можете ли позволить себе товар или услугу по полной цене? Что бы вы ни делали на этом сайте — хотим подчеркнуть: у нас выгодно, интересно и даже увлекательно покупать. КупиКупон — это уникальная возможность сэкономить до 90% на любых покупках в Москве, будь то услуга посещения салона красоты или приобретение смартфона ! Поднимайте себе настроение, забудьте о проблемах, и пусть знакомые завидуют тому, как вам удается всегда хорошо выглядеть, обедать в лучших ресторанах и покупать дорогие гаджеты. По-этому переходим по ссылочке и снова же покупаем по дешевке все что захотим -> {link_cupon_2}')

baza_email = []

@bot.message_handler(commands=['email'])
def email_in_baza(message):
    bot.send_message(message.chat.id, f'Email-адресса в базе : {baza_email}')

@bot.message_handler(commands=['send_message'])
def send_message(message):
    try:
        smtpObj = smtplib.SMTP("smtp.gmail.com", 587) 
        smtpObj.starttls()
        smtpObj.login("kolya.com145@gmail.com", "Kolya14102005") 
        for i in baza_email:
            smtpObj.sendmail("kolya.com145@gmail.com", "kolya.com145@gmail.com", i)
    finally:
        smtpObj.quit()
        baza_email.clear()
        bot.send_message(message.chat.id, 'Сообщения все отправлены и список очищен')

@bot.message_handler(content_types=['text'])
def all(message):
    if message.text.lower() == 'регистрация':
        bot.send_message(message.chat.id, 'Для регистрации укажите ваш email,куда мы сможем вам отправлять информацию 😏') 
    
    elif message.text.lower() == 'буксы':
        murkup_inline_bux = types.InlineKeyboardMarkup()
        button_bux_1 = types.InlineKeyboardButton(text = '1', callback_data = 'bux_1')
        button_bux_2 = types.InlineKeyboardButton(text = '2', callback_data = 'bux_2')
        button_bux_3 = types.InlineKeyboardButton(text = '3', callback_data = 'bux_3')
        button_bux_4 = types.InlineKeyboardButton(text = '4', callback_data = 'bux_4')
        button_bux_5 = types.InlineKeyboardButton(text = '5', callback_data = 'bux_5')
        murkup_inline_bux.add(button_bux_1, button_bux_2, button_bux_3, button_bux_4, button_bux_5)
        bot.send_message(message.chat.id, 'Выберите № букса : ', reply_markup = murkup_inline_bux)

    elif message.text.lower() == 'накрутка':
        murkup_inline_nakrutka = types.InlineKeyboardMarkup()
        button_nakrutka_1 = types.InlineKeyboardButton(text = '1', callback_data = 'nakrutka_1')
        button_nakrutka_2 = types.InlineKeyboardButton(text = '2', callback_data = 'nakrutka_2')
        button_nakrutka_3 = types.InlineKeyboardButton(text = '3', callback_data = 'nakrutka_3')
        murkup_inline_nakrutka.add(button_nakrutka_1, button_nakrutka_2, button_nakrutka_3)
        bot.send_message(message.chat.id, 'Выберите № сервиса для накрутки : ', reply_markup = murkup_inline_nakrutka)

    elif message.text.lower() == 'купоны':
        murkup_inline_cupon = types.InlineKeyboardMarkup()
        button_cupon_1 = types.InlineKeyboardButton(text = '1', callback_data = 'cupon_1')
        button_cupon_2 = types.InlineKeyboardButton(text = '2', callback_data = 'cupon_2')
        murkup_inline_cupon.add(button_cupon_1, button_cupon_2)
        bot.send_message(message.chat.id, 'Выберите № сервиса купонов : ', reply_markup = murkup_inline_cupon)

    elif message.text.lower() == 'школа':
        link_school = 'http://catcut.net/o8dM'
        bot.send_message(message.chat.id, f'Один из лидеров в сфере дистанционного образования, использует фокус на востребованные профессии через инновационные методологии онлайн-обучения. Каждый найдет для себя профессии будущего по таким направлениям как: программирование, веб-дизайн, интернет-маркетинг и управление. Выбирай свою професию и учись вместе с нами -> {link_school}')

    elif message.text.lower() == 'игры':
        link_game = 'http://catcut.net/ZodM'
        link_insta = 'http://instagram.com/bot_zarobotok_bot'
        bot.send_message(message.chat.id, f'Здравствуйте,я предлагаю вам заработать просто играя в игру (плачу я со своего кошелька). Все что вам нужно сделать - это перейти по ссылке {link_game} , зарегистрироваться в игре, зайти в игру(можно сразу выйти,но зайти обязательно),подождать 3 часа,снова зайти в игру и поиграть не меньше часа. Делаете все скриншоты и отправляете сюда {link_insta} , я проверю и если все правильно сделано заплачу 15р (ВАЖНО : плачу только 1 человеку,тоисть с одного и того же IP регистрировать много аккаунтов и присылать мне не нужно - оплаты НЕ БУДЕТ)')

    elif message.text.lower() == 'statistic_change':
        global statistic_num 
        statistic_num = statistic_num - 1
        bot.send_message(message.chat.id, 'Статистика отнялась на -1 ')        

    for baza in message.text:
        if baza == '@':
            bot.send_message(message.chat.id, 'Спасибо,что остались с нами. Вы точно не пожалеете😉')
            bot.send_message(message.chat.id, 'Если хочешь узнать когда начнется рассылка -> Введи команду : /statistic')
            baza_email.append(message.text)
            bot.send_message(message.chat.id, 'Введите команду /earn_money , если хотите просмотреть список дополнительных способов заработка и заработать прямо сейчас')

if __name__ == "__main__":
    bot.infinity_polling()