from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from private.config import bot_token

bot = Bot(bot_token)
dp = Dispatcher(bot,storage=MemoryStorage())
storage = MemoryStorage()