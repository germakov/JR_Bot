"""Файл с основными обработчиками бота."""

import asyncio
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /start."""
    keyboard = [
        [InlineKeyboardButton("🎲 Рандомный факт", callback_data="random_fact")],
        [InlineKeyboardButton("🤖 ChatGPT", callback_data="gpt_interface")],
        [InlineKeyboardButton("👥 Диалог с личностью", callback_data="talk_interface")],
        [InlineKeyboardButton("🧠 Квиз", callback_data="quiz_interface")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "🎉 <b>Добро пожаловать в ChatGPT бота!</b>\n\n"
        "🚀 <b>Доступные функции:</b>\n"
        "• Рандомный факт - получи интересный факт\n"
        "• ChatGPT - общение с ИИ\n"
        "• Диалог с личностью - говори с известными людьми\n"
        "• Квиз - проверь свои знания\n\n"
        "Выберите функцию из меню ниже:"
    )

    if update.message:
        await update.message.reply_text(
            welcome_text, parse_mode="HTML", reply_markup=reply_markup
        )
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            welcome_text, parse_mode="HTML", reply_markup=reply_markup
        )


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка нажатий кнопок главного меню"""
    query = update.callback_query
    await query.answer()


async def start_menu_again(query):
    """Возврат в главное меню (оставлено для совместимости)"""
    keyboard = [
        [InlineKeyboardButton("🎲 Рандомный факт", callback_data="random_fact")],
        [InlineKeyboardButton("🤖 ChatGPT", callback_data="gpt_interface")],
        [InlineKeyboardButton("👥 Диалог с личностью", callback_data="talk_interface")],
        [InlineKeyboardButton("🧠 Квиз", callback_data="quiz_interface")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        "🎉 <b>Добро пожаловать в ChatGPT бота!</b>\n\n"
        "Выберите одну из доступных функций:",
        parse_mode="HTML",
        reply_markup=reply_markup,
    )
