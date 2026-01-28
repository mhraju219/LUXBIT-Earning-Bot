import requests
import time
import os

BOT_TOKEN = os.getenv("8355895167:AAG17a8lmiYRujt7-6LNjqTQvDPoyeOx7lc")
CHANNEL_ID = os.getenv("1003738328507")

while True:
    text = "🔥 Auto post from Render\n👉 https://t.me/yourchannel"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_ID,
        "text": text tes
    }

    requests.post(url, data=data)
    time.sleep(3600)  # post every 1 hour
