Project Statement - WhatsApp Message Scheduler

**Problem Statement**
.In today's fast-paced world, people often forget to send important messages (like birthday wishes, reminders, meeting alerts, or festive greetings) at the right time. 
.Manually remembering and sending messages at specific times is inconvenient and unreliable. 
.There is a need for a simple, automated tool that allows users to schedule WhatsApp messages to be sent automatically at a predetermined date and time.

**Scope of the Project**
This project is a lightweight, console-based **WhatsApp Message Scheduler** built using Python 3.14.0 and the **Twilio Programmable Messaging API** (Whatsapp sandbox). It enables the  users to:
-> Schedule a single WhatsApp message to be sent at a specific future date and time.
-> Receive real-time countdown feedback while the program waits.
-> Automatically send the message when the scheduled time arrives.

**Future Scope of the project (with paid Twilio account):**
-> Send messages to any WhatsApp number (no sandbox restriction)
-> Schedule multiple messages
-> GUI interface
-> Persistent scheduling (even after system restart or shuts down temporarily)
-> Recurring message support
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Target Users**
-> Students who want to automate birthday/reminder messages
-> Individuals who wish to send timed greetings (festivals, anniversaries, etc.)
-> Developers learning Twilio API and automation
-> Setting reminders and alerts
-> Anyone interested in simple scheduling tools without third-party apps

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 **High-Level Features**
 
1. **User-Friendly Input System**
   -> Enter receiver name, WhatsApp number, message, date (YYYY-MM-DD), and time (HH:MM in 24-hour format)

2. **Input Validation**
   -> Checks for empty messages
   -> Validates date-time format
   -> Prevents scheduling in the past

3. **Real-Time Countdown**
   -> Displays remaining time in minutes and seconds
   -> Updates every 40 seconds during wait

4. **Automated Message Delivery**
   -> Uses Twilio's official WhatsApp API
   -> Sends message exactly at the scheduled time
   -> Shows success/failure status with Message SID

5. **Secure Credential Handling**
   ->Twilio Account SID and Auth Token are stored in variables (recommended to use environment variables in production)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Submitted By**
**Tanishka Sahu**  
Registration No: 25BCE10056  
B.Tech CSE - 1st Year -SCOPE 
VIT Bhopal University
---------------------------------------------------
Professor: DR. AVR MAYURI
SLOT: A11+A12+A13
---------------------------------------------------
