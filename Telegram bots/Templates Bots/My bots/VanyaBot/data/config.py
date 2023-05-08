import json
from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env("ADMINS").split(',')  # Тут у нас будет список из админов
#ADMINS = [i for i in env("ADMINS").split(",")] 
DB_STR = env.str("DB_STR")  # Строка подключения к базе
GROUP_URL = env.str("GROUP_URL") # Ссылка на группу
GROUP_ID = env.str("GROUP_ID") # Id группы
