import os
from dotenv import load_dotenv

load_dotenv()

bot_token = str(os.getenv('token'))
group_id = str(os.getenv('group_id'))