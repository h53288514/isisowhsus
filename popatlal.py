import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 27003494
api_hash = '651b80af49ba598ab137237c87f4b3b4'
session_string = 'your_session_string_here'

receiver = '@tsar_almis'
message = 'bhai tum op ho'
count = 7
delay = 1

with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
    for i in range(1, count + 1):
        full_message = f"{message} #{i}"
        client.send_message(receiver, full_message)
        print(f"Sent: {full_message}")
        time.sleep(delay)

print("All messages sent successfully.")
