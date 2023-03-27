from telegram import Update
from telegram.ext import ContextTypes

from .config import RUN_TIMES
from .database import create_session
from .models import Dictionary


async def get_five_eng_words(context: ContextTypes.DEFAULT_TYPE):
    job = context.job

    message = ""
    session = create_session()
    words = Dictionary.get_random_words(session)
    for word in words:
        message += f"-- {word.word.capitalize()} ({word.pronounce})\n{word.detail}\n"

    await context.bot.send_message(chat_id=job.chat_id, text=message)


async def study(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    # for run_time in RUN_TIMES:
    #     context.job_queue.run_daily(
    #         get_five_eng_words,
    #         time=run_time,
    #         chat_id=chat_id,
    #         name=str(chat_id),
    #     )

    context.job_queue.run_repeating(
        get_five_eng_words,
        10,
        chat_id=chat_id,
        name=str(chat_id),
        data=10
    )

    await context.bot.send_message(
        chat_id=chat_id, text="Scheduled messages are set!")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
