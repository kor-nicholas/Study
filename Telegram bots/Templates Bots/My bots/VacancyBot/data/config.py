from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
db_sql = env.str("db_sql") # База данных
group_id = env.str('GROUP_ID') # id группы, куда кидать заявки
feedback_nick = env.str('FEEDBACK') # ник пользователя поддержки
