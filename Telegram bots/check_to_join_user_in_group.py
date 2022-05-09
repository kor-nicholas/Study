

@bot.message_handler(commands=['start'])
    def start(message):
        user_id = message.chat.id
        my_channel_id = -1001337625079
        statuss = ['creator', 'administrator', 'member', 'left']

        status = await bot.get_chat_member(chat_id=my_channel_id, user_id=message.from_user.id).status

        if status == 'administrator':
            pass
        elif status == 'creator':
            pass
        elif status == 'member':
            pass
        elif status == 'left':
            await bot.send_message(message.chat.id, "Подпишись на канал {} для продолжения".format(set_channel))



        