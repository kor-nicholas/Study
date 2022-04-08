

user_channel_status = await bot.get_chat_member(chat_id=channel, user_id=message.from_user.id)
    if user_channel_status["status"] != "left":

    	