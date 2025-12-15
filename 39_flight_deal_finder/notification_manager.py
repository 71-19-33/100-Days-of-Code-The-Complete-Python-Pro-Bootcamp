import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ["TWILIO_SID"]
        self.auth_token = os.environ["TWILIO_TOKEN"]
        self.twilio_nr = "+17439626778"
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, message:str):
        if message != "":
            self.client.messages.create(body=message, from_=self.twilio_nr, to=os.environ["MY_PHONE_NUMBER"])
