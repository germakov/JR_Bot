import os

from dotenv import load_dotenv

load_dotenv()

TG_BOT_TOKEN = os.getenv("TG_TOKEN")
CHATGPT_TOKEN = os.getenv("GPT_TOKEN")

if not all([TG_BOT_TOKEN, CHATGPT_TOKEN]):
    raise ValueError("Введите токены в .env")
