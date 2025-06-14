import logging

from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from config import CHATGPT_TOKEN, TG_BOT_TOKEN
from handlers import basic, random_fact

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    try:
        application = Application.builder().token(TG_BOT_TOKEN).build()
        application.add_handler(CommandHandler("start", basic.start))
        # application.add_handler(CommandHandler("random", random_fact.random_fact))
        # application.add_handler(
        #     CallbackQueryHandler(random_fact.random_fact_callback, pattern="^random_")
        # )
        application.add_handler(CallbackQueryHandler(basic.menu_callback))
        application.add_handler(CallbackQueryHandler(button))

        logger.info("Бот запущен...")

        application.run_polling()
    except Exception as e:
        logger.error(f"Ошибка при запуске {e}")


if __name__ == "__main__":
    main()
