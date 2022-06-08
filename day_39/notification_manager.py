from twilio.rest import Client
import os
import dotenv
from pathlib import Path

dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)

# Environment variables
twilio_sid = os.environ["TW_ACCOUNT_SID"]
twilio_token = os.environ["TW_AUTH_TOKEN"]
twilio_from = os.environ["TW_FROM_NUMBER"]
twilio_to = os.environ["TW_TO_NUMBER"]


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self):
        self.client = Client(twilio_sid, twilio_token)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_from,
            to=twilio_to
        )
        print(message.sid)
