import os

from dotenv import load_dotenv

load_dotenv()

CHATGPT_TOKEN = os.getenv(CHAT_GPT_TOKEN)
TG_BOT_TOKEN = os.getenv(TGBOT_TOKEN)

if not all((TG_BOT_TOKEN, CHATGPT_TOKEN)):
    raise ValueError("Введите токены в .env")
