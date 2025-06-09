import os

from dotenv import load_dotenv

load_dotenv()

TG_BOT_TOKEN = os.getenv(TGBOT_TOKEN)
GHATGPT_TOKEN = os.getenv(GHAT_GPT_TOKEN)

if not all([TG_BOT_TOKEN, CHATGPT_TOKEN]):
    raise ValueError("Введите токены в .env")
