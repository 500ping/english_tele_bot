import threading
from flask import Flask
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler


from src.handler import study, echo, start
from src.database import create_session
from src.models import Dictionary

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'


@app.route('/import_data')
def import_data():
    session = create_session()
    Dictionary.import_data(session)

    return 'Import done!'


def main() -> None:
    application = ApplicationBuilder().token(
        "5794629205:AAGarmgzhTdFpOeHYLzqB7kqjaOLhq1bRac").build()

    start_handler = CommandHandler('start', start)
    cron_handler = CommandHandler('study', study)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(cron_handler)
    application.add_handler(echo_handler)

    application.run_polling()


class FlaskThread(threading.Thread):
    def run(self) -> None:
        app.run(host="0.0.0.0")


class TelegramThread(threading.Thread):
    def run(self) -> None:
        main()


if __name__ == "__main__":
    flask_thread = FlaskThread()
    flask_thread.start()

    main()
