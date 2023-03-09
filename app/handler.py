import pytz
import datetime
from telegram import Update
from telegram.ext import ContextTypes


async def send_message(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    await context.bot.send_message(
        chat_id=job.chat_id, text="Hello, it's time for your scheduled message!")


async def run_cron(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(context)
    chat_id = update.effective_chat.id
    context.job_queue.run_daily(
        send_message,
        time=datetime.time(hour=11, minute=22,
                           tzinfo=pytz.timezone("Asia/Bangkok")),
        chat_id=chat_id,
        name=str(chat_id),
    )
    await context.bot.send_message(
        chat_id=chat_id, text="Scheduled messages are set!")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
