# Получить реф ссылку

@dp.message_handler()
async def pars(msg:types.Message):
    if msg.text == "Получить реф ссылку":
        me = await bot.get_me()
        await bot.send_message(msg.from_user.id, str(msg.from_user.id))
        await bot.send_message(msg.from_user.id, f"\n\n\nВаша реферальная ссылка:\nhttps://t.me/{me.username}?start={msg.chat.id}")

# Регистрация пользователя

def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None


@dp.message_handler(commands=["start"], state="*")
async def user_registration(message: types.Message):
    unique_code = extract_unique_code(message.text)
    if unique_code and str(unique_code) != str(message.from_user.id):
        print(unique_code)
        await bot.send_message(unique_code, f"@{message.from_user.username} перешел по твоей ссылке")
        if data.get(str(unique_code)) == False:
            data.set(str(unique_code), [(str(message.from_user.id))])
        elif len(list(data.get(str(unique_code)))) > 0 and str(message.from_user.id) not in data.get(str(unique_code)):   
            if str(message.from_user.id) == unique_code:
                await bot.send_message(message.from_user.id, "Ты не можешь пригласить сам себя)")
            else:
                s = data.get(str(unique_code))
                s.append(str(message.from_user.id))
                data.set(str(unique_code), s)
    else:
        pass
    
    await bot.send_message(message.from_user.id, "Привет!", reply_markup=markup)




