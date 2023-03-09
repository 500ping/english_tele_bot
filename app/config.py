import os
import pytz
import datetime

TZ = "Asia/Bangkok"

API_TOKEN = os.getenv("API_TOKEN")
RUN_TIMES = [
    datetime.time(
        hour=11,
        minute=22,
        tzinfo=pytz.timezone("Asia/Bangkok")
    )
]
