import os
import requests
import random
import time
from telegram import Bot

# Telegram bot setup
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

bot = Bot(token=BOT_TOKEN)

# Example quotes
quotes = [
    "Even the darkest night will end and the sun will rise.",
    "Dreams don't work unless you do.",
    "Be patient. Sometimes you have to go through the worst to get the best.",
    "Pain is temporary, greatness lasts forever.",
    "Don’t watch the clock; do what it does — keep going."
]

while True:
    quote = random.choice(quotes)
    bot.send_message(chat_id=CHANNEL_ID, text=quote)
    time.sleep(43200)  # 12 hours (2 posts per day)
