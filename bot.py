import requests
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

while True:
    text = "🔥 Auto post from Render\n👉 https://t.me/yourchannel"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_ID,
        "text": text
    }

    requests.post(url, data=data)
    time.sleep(3600)  # post every 1 hour
