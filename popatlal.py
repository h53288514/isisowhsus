import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 27003494
api_hash = '651b80af49ba598ab137237c87f4b3b4'
session_string = '1BVtsOLYBu2RvSHMOwndCXhiZ0slvK4lYnE3U1rqm0f1OKuS4wZq0K5L-s4h-laddQQjXu1BoP31T-WuBudkkzLAlhYwH0aWgiKxFbYAV11cqGajk7sXbvXPbt5VlsSI4j6ZWQYhz6FQrZO3Q29YXtpbfYoEj6uQfz5D_fpc-mT0TABcUdJFYnxxv0c9qvIT4Bt_q8TbFFZQl5FRFwhNjg4AIwf8gUZwPBhFX9Mm6kNfnuTeNjlJOI2qTr_3vroTlBgCYhhF6kKvVJPnrc27bkGpHdSzA9Qo2J22UtG7MPk0NQ3BtrodI68nw0IpNnfviyMWC4wdbF-GoyNhVspYMhhyRe1YOzbU='

receiver = '@tsar_almis'
message = 'bhai tum op ho'
count = 7
delay = 1  # seconds

with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
    for i in range(count):
        client.send_message(receiver, f"{message} #{i+1}")
        print(f"Sent: {message} #{i+1}")
        time.sleep(delay)
