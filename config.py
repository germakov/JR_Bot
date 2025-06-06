import os

from dotenv import load_dotenv

load_dotenv()

TG_BOT_TOKEN = os.getenv(TG_BOT_TOKEN)
GHATGPT_TOKEN = os.getenv(GHATGPT_TOKEN)

if not all([TG_BOT_TOKEN, CHATGPT_TOKEN]):
    raise ValueError("Введите токены в .env")
