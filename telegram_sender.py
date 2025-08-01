from telethon.sync import TelegramClient
import os
import time
import random

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone_number = os.getenv("PHONE_NUMBER")

group_links = [
    "https://t.me/group1",
    "https://t.me/group2",
    "https://t.me/group3"
]

message = "Hello! This is your auto-sent message. ✅ Works every 5 mins!"

with TelegramClient("session", api_id, api_hash) as client:
    for group in group_links:
        try:
            client.send_message(group, message)
            print(f"✅ Message sent to {group}")
            delay = random.randint(60, 75)
            print(f"⏳ Waiting {delay}s before next group...")
            time.sleep(delay)
        except Exception as e:
            print(f"❌ Failed to send to {group}: {e}")
