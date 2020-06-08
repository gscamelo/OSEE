#!/usr/bin/python
#Python script that send your phone number a text as soon as Black Hat 2019 training goes live using Twilio
#The script can be coupled with cronjob that runs every hour or whatever you may see fit
#Crontab => */5 * * * * python3 BH21RegChecker.py

from twilio.rest import Client
import requests

account_sid = '<your Twilio account SID>'
auth_token = '<your Twilio authentication token>'
client = Client(account_sid, auth_token)

def Send(Message):
    client.messages.create(
        to='<your phone number>',
        from_='<Twilio virtual phone number>',
        body=Message,
    )

def main():
    message = 'Blackhat 2021 training page is live! Go register now!!'
    
    # test case
    #r = requests.get('https://www.blackhat.com/us-20/')
    r = requests.get('https://www.blackhat.com/us-21/')
    print(r.status_code)
    if r.status_code != 404:
        Send(message)

if __name__ == '__main__':
    main()