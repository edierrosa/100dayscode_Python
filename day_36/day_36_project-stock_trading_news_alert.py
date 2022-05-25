import requests
import dotenv
from pathlib import Path
import os
from twilio.rest import Client

# Environment variables
dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)
# print(dotenv_path.exists())

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


# Check stock price movement
def check_stock_price():
    alphavantage_endpoint = os.environ["APLHAVANTAGE_ENDPOINT"]
    alphavantage_apikey = os.environ["ALPHAVANTAGE_APIKEY"]
    alpha_param = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": alphavantage_apikey
    }
    alphavantage_response = requests.get(
        alphavantage_endpoint, params=alpha_param)
    alphavantage_response.raise_for_status()
    alphavantage_data = [value for (key, value) in alphavantage_response.json()[
        "Time Series (Daily)"].items()]

    yesterday_close = float(alphavantage_data[0]["4. close"])
    db_yesterday_close = float(alphavantage_data[1]["4. close"])

    stock_diff = abs(yesterday_close - db_yesterday_close)
    stock_ppo = (stock_diff / yesterday_close) * 100

    return stock_ppo > 1


# Get News
def get_news():
    newsapi_endpoint = os.environ["NEWSAPI_ENDPOINT"]
    newsapi_key = os.environ["NEWSAPI_KEY"]
    newsapi_param = {
        "qInTitle": COMPANY_NAME,
        "sortBy": "popularity",
        "apiKey": newsapi_key,
    }

    newsapi_response = requests.get(newsapi_endpoint, params=newsapi_param)
    newsapi_response.raise_for_status()
    newsapi_data = newsapi_response.json()[
        "articles"][:3]
    articles = [
        f"Headline: {article['title']}." for article in newsapi_data]
    return articles


# Send a separate message with the percentage change and each article's title and description to your phone number
def sms_news():
    tw_account_sid = os.environ["TW_ACCOUNT_SID"]
    tw_auth_token = os.environ["TW_AUTH_TOKEN"]
    tw_from_number = os.environ["TW_FROM_NUMBER"]
    tw_to_number = os.environ["TW_TO_NUMBER"]

    client = Client(tw_account_sid, tw_auth_token)
    for article in get_news():
        message = client.messages.create(
            body=article,
            from_=tw_from_number,
            to=tw_to_number
        )
        print(message.status)


if check_stock_price():
    sms_news()
