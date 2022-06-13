from twilio.rest import Client
import os
import dotenv
from pathlib import Path
from smtplib import SMTP

dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)

# Environment variables
twilio_sid = os.environ["TW_ACCOUNT_SID"]
twilio_token = os.environ["TW_AUTH_TOKEN"]
twilio_from = os.environ["TW_FROM_NUMBER"]
twilio_to = os.environ["TW_TO_NUMBER"]
smtp_mail = os.environ["SMTP_YAHOO"]
user_mail = os.environ["USER_YAHOO"]
mail_password = os.environ["PASSWORD_YAHOO"]


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

    def send_mail(self, emails, message, flight_link):
        """Send mail to specified address"""
        with SMTP(smtp_mail, port=587) as connection:
            connection.starttls()
            connection.login(user=user_mail, password=mail_password)
            for email in emails:
                connection.sendmail(from_addr=user_mail,
                                    to_addrs=email,
                                    msg=f"Subject: Low Price Flight\n\n{message}\n{flight_link}".encode(
                                        "utf-8")
                                    )
