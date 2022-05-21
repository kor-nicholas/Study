import logging

from aiogram import Bot, Dispatcher
from config import bot_token
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )