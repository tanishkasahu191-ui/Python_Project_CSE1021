**WhatsApp Message Scheduler**
A simple Python-based tool that lets you schedule and automatically send WhatsApp messages at your desired date and time using the **Twilio WhatsApp API**.
by **Tanishka Sahu**  
Registration No: 25BCE10056 | CSE-SCOPE 1st Year | VIT BHOPAL UNIVERSITY
-----------------------------------------------------------------------------


**Overview of the Project

This is a console-based **WhatsApp Message Scheduler** that allows users to:
- Schedule a WhatsApp message to be sent automatically on a specific future date and time.
- See a live countdown until the message is sent.
- Send the message instantly when the scheduled time arrives — fully automated!

Perfect for birthday wishes, reminders, meeting alerts, festival greetings, etc.

> Currently uses **Twilio's free WhatsApp Sandbox** (great for testing and personal use).

**
----------------------------------------------------------------------

**Features

- Schedule messages for any future date & time  
- Input validation (date, time, empty message check)  
- Live countdown timer (updates every 40 seconds)  
- Automatic message sending using Twilio API  
- Success/Failure feedback with Message SID  
- Beginner-friendly and fully functional  

**
-------------------------------------------------------------------------------

**Technologies / Tools Used

 Technology  and  Purpose                       
 Python 3.14.0   ------>       Core programming language        
 Twilio SDK   ---->     Sending whatsApp messages (An API which is tied up with whatsApp)       
 datetime, time  ----->  handling scheduling & countdown  
 Twilio whatsApp Sandbox -----> free testing environment     **

 ------------------------------------------------------------------------

** STEPS TO INSTALL AND RUN THE PROJECT
- Python 3 installed
- A free [Twilio Account](https://www.twilio.com/try-twilio)
- WhatsApp Sandbox activated
 **

-Install Twilio library
pip install twilio   (run it in terminal to install twilio library)
-Get your Twilio credentials
.Go to https://console.twilio.com
.Copy your Account SID and Auth Token

-Join Twilio WhatsApp Sandbox
Open WhatsApp and send join <your-sandbox-code> to:text+1 415 523 8886
Your contact number is now connected.

-Update the code with your credentials
-Run the program
-Enter details when prompted
Receiver name,
Receiver WhatsApp number (with country code ; example: +91987654XXXX),
Message,
Date (YYYY-MM-DD),
Time (HH:MM in 24-hour format),


Now,The program will wait and send the message automatically
The message will be recieved by the number user entered.
----------------------------------------------------------------
**Instructions for Testing

-Use your own WhatsApp number as the receiver for testing.
-Schedule a message 1–2 minutes in the future.
-Watch the live countdown.
-When time reaches zero → Message will be sent!
-You’ll receive it on WhatsApp and see "Message sent successfully!" in terminal.

NOTE: Keep the terminal/program running until it is (the message) is sent.**


------------------------------------------------------
**SCREENSHOTS**
![screenshot of output](https://github.com/user-attachments/assets/21b1ca0b-30d6-4a07-8adc-6a7771e9d041)
![whatsapp message recieved screenshot](https://github.com/user-attachments/assets/9f7fd5a0-82ed-47d0-830d-49ce2043797d)
![twilio  setup on whatsapp screenshot](https://github.com/user-attachments/assets/2ff7a5ed-9a33-48f2-a6b9-2521bab72465)
![screenshot of hidden twilio credentials](https://github.com/user-attachments/assets/ea8be26b-2b96-42b2-85c0-3529eb63bce1)



