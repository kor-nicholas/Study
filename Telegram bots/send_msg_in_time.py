import schedule

def messege():
    bot.send_message(message.chat.id, 'Привет! Я сообщение, отправленное в 7 часов утра.')

schedule.every().day.at("07:00").do(messege)
while True:
    schedule.run_pending()
    time.sleep(1)