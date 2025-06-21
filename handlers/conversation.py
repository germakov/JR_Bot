from warnings import filterwarnings

from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ConversationHandler, MessageHandler, filters)
from telegram.warnings import PTBUserWarning

from handlers import (basic, chatgpt_interface, personality_chat, quiz,
                      random_fact)

filterwarnings(
    action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning
)

gpt_conversation = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(chatgpt_interface.gpt_start, pattern="^gpt_interface$")
    ],
    states={
        chatgpt_interface.WAITING_FOR_MESSAGE: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                chatgpt_interface.handle_gpt_message,
            )
        ],
    },
    fallbacks=[
        CommandHandler("start", basic.start),
        CallbackQueryHandler(basic.menu_callback, pattern="^(gpt_finish|main_menu)$"),
    ],
    per_message=True,
)

personality_conversation = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(personality_chat.talk_start, pattern="^talk_interface$"),
        CommandHandler("talk", personality_chat.talk_command),
    ],
    states={
        personality_chat.SELECTING_PERSONALITY: [
            CallbackQueryHandler(
                personality_chat.personality_selected, pattern="^personality_"
            )
        ],
        personality_chat.CHATTING_WITH_PERSONALITY: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                personality_chat.handle_personality_message,
            ),
            CallbackQueryHandler(
                personality_chat.handle_personality_callback,
                pattern="^(continue_chat|change_personality|finish_talk)$",
            ),
        ],
    },
    fallbacks=[
        CommandHandler("start", basic.start),
        CallbackQueryHandler(basic.menu_callback, pattern="^main_menu$"),
    ],
    per_message=True,
)

quiz_conversation = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(quiz.quiz_start, pattern="^quiz_interface$"),
        CommandHandler("quiz", quiz.quiz_command),
    ],
    states={
        quiz.SELECTING_TOPIC: [
            CallbackQueryHandler(quiz.topic_selected, pattern="^quiz_topic_")
        ],
        quiz.ANSWERING_QUESTION: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, quiz.handle_quiz_answer),
            CallbackQueryHandler(
                quiz.handle_quiz_callback,
                pattern="^(quiz_continue_|quiz_change_topic|quiz_finish)$",
            ),
        ],
    },
    fallbacks=[
        CommandHandler("start", basic.start),
        CallbackQueryHandler(basic.menu_callback, pattern="^main_menu$"),
    ],
    per_message=True,
)
