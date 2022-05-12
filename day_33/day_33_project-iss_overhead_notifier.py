from datetime import datetime
import requests
import re
from smtplib import SMTP
import time

MY_LAT = -27.053770
MY_LNG = -49.543880
ADDRESS = "someemail@provider.com"


def iss_close():
    """Check if I am close to iss"""

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5


def check_night():
    """Check if it is night """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    time_now = datetime.now()

    response_mylocal = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response_mylocal.raise_for_status()
    data_mylocal = response_mylocal.json()
    sunrise_mylocal = datetime.strptime(
        (re.split(r"T|\+", data_mylocal["results"]["sunrise"])[1]), "%H:%M:%S")
    sunset_mylocal = datetime.strptime(
        (re.split(r"T|\+", data_mylocal["results"]["sunset"])[1]), "%H:%M:%S")

    return time_now >= sunset_mylocal or time_now <= sunrise_mylocal


def send_mail(address):
    """Send mail to specified address"""
    my_mail = "someemail@someprovider.com"
    mail_password = "somepassword"
    with SMTP("smtp.server", port=587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=mail_password)
        connection.sendmail(from_addr=my_mail,
                            to_addrs=address, msg="Subject:ISS above\n\n Look up mate!")


while True:
    time.sleep(60)
    if iss_close() and check_night():
        send_mail(ADDRESS)
