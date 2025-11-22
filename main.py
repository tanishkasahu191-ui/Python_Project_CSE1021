# Made by: Tanishka Sahu (CSE 1st Year)
# Roll No: 25BCE10056
# This program sends a WhatsApp msg on a selected date & time
# Using Twilio API

from twilio.rest import Client
from datetime import datetime
import time
import sys

# Twilio acc details (keeping blank for safety)
account_sid = "AC370f4371c8c3b0d76ccb406af1c9847e" #PUT YOUR ACC SID HERE"
auth_token = "a45ab5294e1b44cbb17a8ec8bb4cad10" #PUT YOUR AUTHORIZED TOKEN"

# official WhatsApp sandbox number
twilio_whno = "whatsapp:+14155238886"

# making client object one time
client = Client(account_sid, auth_token)

print("---- WhatsApp Message Scheduler ----")
print("(Make sure sandbox is connected properly!)")

# taking inputs
receiver_name = input("Enter receiver name: ").strip()
receiver_num = input("Enter WhatsApp number with country code: ").strip()

msg_text = input("Type your message: ").strip()
if msg_text == "":
    print("Message cannot be empty!")
    sys.exit()

print("Now enter Date and Time when message should be sent")
date_inp = input("Date (YYYY-MM-DD): ")
time_inp = input("Time (HH:MM 24hr): ")

#  date+time
try:
    finaltime = datetime.strptime(date_inp+" "+time_inp, "%Y-%m-%d %H:%M")
except:
    print("Invalid date or time format!")
    sys.exit()

currenttime = datetime.now()

# check if time is not older
if finaltime <= currenttime:
    print("Error: You entered past/current time.")
    sys.exit()

# calculate waiting seconds
waitsec = (finaltime - currenttime).total_seconds()

print(f"Message scheduled for {receiver_name} at {finaltime}")
print(f"Waiting approx {int(waitsec//60)} mins.....")

# small waiting loop
for left in range(int(waitsec), 0, -40):
    m = left // 60
    s = left % 60
    print(f"Time left: {m} min {s} sec", end="")
    time.sleep(40 if left > 40 else left)

print("Sending message now..")

def send_msg():
    try:
        sent = client.messages.create(
            from_=twilio_whno,
            body=msg_text,
            to=f"whatsapp:{receiver_num}"
        )
        print("Message sent successfully!")
        print("SID:", sent.sid)
    except Exception as err:
        print("Message sending failed!")
        print("Error:", err)

# calling function now
send_msg()

print("Done. Program finished.")
input("Press Enter to exit...")