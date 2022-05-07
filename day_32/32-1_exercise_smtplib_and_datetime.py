from smtplib import SMTP
import datetime as dt
import random

mail_1 = "someemail@someprovider.com"
mail_2 = "someemail@someprovider.com"
mail_2_password = "somepassword"


# Current day
days_of_week = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
now = dt.datetime.now()
day_of_week = days_of_week[now.weekday()]


if day_of_week == "Saturday":
    # Create a list of quotes
    with open("./day_32/quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        todays_quote = random.choice(quotes_list).strip()

    # Create message
    mail_msg = f"Subject:{day_of_week} quote\n\n" + todays_quote

    # Sending today's quote email
    with SMTP("smtp.server", port=587) as connection:
        connection.starttls()
        connection.login(user=mail_2, password=mail_2_password)
        connection.sendmail(from_addr=mail_2, to_addrs=mail_1, msg=mail_msg)
