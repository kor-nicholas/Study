from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести список команд бота"),
            types.BotCommand("myid", "Узнать свой (группы) ID")
        ]
    )