

import logging
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler

from app.config import API_TOKEN
from app.handler import study, echo, start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__ == '__main__':
    application = ApplicationBuilder().token(API_TOKEN).build()

    start_handler = CommandHandler('start', start)
    cron_handler = CommandHandler('study', study)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(cron_handler)
    application.add_handler(echo_handler)

    application.run_polling()
