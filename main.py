"""Здесь происходит создание и запуск бота и его основных функций"""

import logging

from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ConversationHandler, MessageHandler, filters)
from telegram.warnings import PTBUserWarning

from config import TG_BOT_TOKEN
from handlers import (basic, chatgpt_interface, personality_chat, quiz,
                      random_fact)
from handlers.conversation import *

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

"""Функция создает и запускает бота, а так-же обрабатывает комманды и ответы."""


def main():
    try:
        application = (
            Application.builder().token(TG_BOT_TOKEN).build()
        )  # Создаем Телеграм бота
        """Обработчики входящих комманд"""
        application.add_handler(CommandHandler("start", basic.start))
        application.add_handler(CommandHandler("random", random_fact.random_fact))
        application.add_handler(CommandHandler("gpt", chatgpt_interface.gpt_command))
        application.add_handler(
            CommandHandler("personality", personality_chat.talk_command)
        )
        application.add_handler(CommandHandler("quiz", quiz.quiz_command))

        gpt_conversation
        personality_conversation
        quiz_conversation

        """Обработчики бесед"""
        application.add_handler(quiz_conversation)
        application.add_handler(personality_conversation)
        application.add_handler(gpt_conversation)

        """Обработчики обратного запроса"""
        application.add_handler(
            CallbackQueryHandler(random_fact.random_fact_callback, pattern="^random_")
        )
        application.add_handler(
            CallbackQueryHandler(chatgpt_interface.handle_gpt_message, pattern="^gpt_")
        )
        application.add_handler(CallbackQueryHandler(basic.menu_callback))

        """Запуск бота"""
        logger.info("Бот запущен успешно!")
        application.run_polling()

    except Exception as e:
        logger.error(f"Ошибка при запуске: {e}")


if __name__ == "__main__":
    main()
