import json
import logging
import os
from aiogram import executor
from aiohttp import request

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

from aiogram import types


async def on_startup(dispatcher):

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

async def on_shutdown(dispatcher):
    logging.warning('Shutting down ...')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)






    
