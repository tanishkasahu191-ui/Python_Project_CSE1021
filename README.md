# Python_Project_CSE1021
*SUBMISSION DETAILS*
.Submitter:TANISHKA SAHU
.Reg no.: 25BCE10056
.Subject: Proble solving and Programming (CSE1021)



The project is a Python based Whatsapp automated system built using twilio API. 
The user can type a message , choose a date and time to send the message and the program will automatically deliver that message to the selected  Whatsapp number at the scheduled time.



*KEY FEATURES OF THE PROJECT*
.Sends whatsapp messages using python.
.Uses twilio's official whatsapp api.
.Has simple user input system.
.User can type the message to be delivered at a specific time and date.



*Technologies Used*
>>.Basic Python(conditional statements,user defined functions,modules,import libraries)
>>.Twilio API
>>.Datetime module
>>.Time module



*What is TWILIO and its significance in project. *
>>Twilio is a cloud platform that allows developers send whatsApp messages ,sms,annd calls through simple API code.
>>Python cannot directly send whatsapp messages.So twilio is an approved whatsapp provider ,so it lets your Python program send messages to whatsapp



*Significance of datetime module  and time module in project*
>>The datetime module in Python is used to work with dates and times
>>In this project, it plays an important role because user is allowed to choose a specific date and time for sending messages
>>It also compares the current time and scheduled time so the program can calculate how long it should wait
>>Time module is used to make the program wait (sleep) until it's time to send the whatsApp message.



*Sample input*
Enter the recipient name: Tanishka
Enter the recipient WhatsApp number with country code (e.g. +916783XXXXXX): +917717603726
Enter the message you want to send to Tanishka: hi girl
Enter the date to send the message (YYYY-MM-DD): 2025-11-20
Enter the time to send the message (HH:MM) in 24-hour format: 18:39
Message scheduled for Tanishka at 2025-11-20 18:39.
Waiting 20 seconds...



*Sample Output*
#message will be sent to the whatsApp number entered
Message sent!



*Notes*
>>.Twilio sandbox number must be used for whatsapp.
>>.Account SID and auth token should be added in the code but must be kept privately to avoid cyber crimes.
>>.Works only with approved contact numbers in the twilio Sandbox.



