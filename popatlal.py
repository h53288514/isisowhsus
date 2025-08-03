import sys
import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 27003494
api_hash = '651b80af49ba598ab137237c87f4b3b4'
session_string = '1BVtsOHgBu6oO7owFxFNomC6hWQd84CeF6yEze-u4bN7DfM8tnLmhoBicRKTeahFzwvTHQgM2S5ZbeFwYSUfLkSLxPM2zaCIeICXNWhmaSAb-XE2pzdfxa7CshpUJ_I_oyYETLOb52I29uvknfW2KgSmWWKhEQSS4Jtc2rIBJDpgmKGL7ds-A2F9NdNOO6Fj7IfgSs4VP9f6SqqHHkDi_36cz_dWYMn38vNlyTjPHHjGtxN6iL29UbIVH7Egz7hp-c1M4la2Vh4GaRjrhgKuXykgk4ZNZFihJUKDlOrRLDsmc1JafDRmEvREI5HBE-7lXgCYGRb8L_mW1IhLpnX8ZE3QqscxnWok='  # <-- yehi chhoda hai jaise tha

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
