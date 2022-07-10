from smtplib import SMTP
import requests as r
from bs4 import BeautifulSoup
import os
import dotenv
from pathlib import Path

# Environment variables
dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)

smtp_mail = os.environ["mail smtp"]
user_mail = os.environ["user mail"]
mail_password = os.environ["mail password"]


# Amazon product data
amz_product_url = "amazon url"
amz_headers = {"your headers"}


def get_amazon_price(product_url=amz_product_url, headers=amz_headers):
    amz_request = r.get(product_url, headers=headers).text
    amz_product_soup = BeautifulSoup(amz_request, "html.parser")
    amz_price = float(amz_product_soup.find(
        name="span", class_="a-offscreen").getText().split("$")[1])
    amz_product_title = amz_product_soup.find(
        name="span", id="productTitle").getText(strip=True)
    return amz_price, amz_product_title


# Email notifier
def send_email(msg, emails):
    with SMTP(smtp_mail, port=587) as connection:
        connection.starttls()
        connection.login(user=user_mail, password=mail_password)
        for email in emails:
            connection.sendmail(from_addr=user_mail, to_addrs=email, msg=msg)


# Price trigger
def check_price(target_price, emails, product_link=amz_product_url):
    current_price, product_title = get_amazon_price()
    if current_price <= target_price:
        msg = f"Subject: Amazon Low Price Alert\n\nName,\n{product_title} for ${current_price}\n{product_link}"
        send_email(msg=msg, emails=emails)


emails = ["some emails"]
check_price(300, emails)
