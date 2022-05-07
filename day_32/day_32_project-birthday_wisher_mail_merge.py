import datetime as dt
import pandas as pd
from smtplib import SMTP
import random


# Check today's date
now = dt.datetime.now()
today = dt.date(year=now.year, month=now.month, day=now.day)

# Get data
data = pd.read_csv("./day_32/birthdays.csv")
birthdays = data.to_dict(orient="records")

# Send email


def send_mail(address, birthday_msg):
    """Send mail to specified address"""
    my_mail = "someemail@someprovider.com"
    mail_password = "somepassword"
    with SMTP("smtp.server", port=587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=mail_password)
        connection.sendmail(from_addr=my_mail,
                            to_addrs=address, msg=birthday_msg)

# Create birthday message


def birthday_msg(name):
    letter_number = random.randint(1, 3)
    with open(f"./day_32/letter_templates/letter_{letter_number}.txt") as template:
        birthday_msg = f"Subject: Happy Birthday {name}\n\n" + \
            template.read().replace("[NAME]", name)
        return birthday_msg


# Check if today matches a birthday and send email
for contact in birthdays:
    birthday = dt.date(
        year=today.year, month=contact["month"], day=contact["day"])
    if birthday == today:
        send_mail(address=contact["email"],
                  birthday_msg=birthday_msg(contact["name"]))
