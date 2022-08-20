import requests
from twilio.rest import Client
import dotenv
from pathlib import Path
import os

dotenv_path = Path("path_to_env_file")
dotenv.load_dotenv(dotenv_path=dotenv_path)

# Environment variables
ow_endpoint = os.environ["OW_END_POINT"]
ow_api_key = os.environ["OW_API_KEY"]
tw_account_sid = os.environ["TW_ACCOUNT_SID"]
tw_auth_token = os.environ["TW_AUTH_TOKEN"]
tw_from_number = os.environ["TW_FROM_NUMBER"]
tw_to_number = os.environ["TW_TO_NUMBER"]

# OW parameters
parameters = {
    "lat": "your_latitude_integer",
    "lon": "your_longitude_integer",
    "appid": ow_api_key,
    "exclude": "current,minute,daily",
}


# OW API call 12 hours weather condition
response = requests.get(ow_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]
# weather_condition_id = [weather_condition["weather"][0]["id"] for weather_condition in hourly_data]


# Check for rain or snow
def bring_umbrella():
    for weather_condition in hourly_data:
        if int(weather_condition["weather"][0]["id"]) < 700:
            return True


# Define alert message
if bring_umbrella():
    weather_alert = "Bring an umbrella!"
else:
    weather_alert = "It won't rain today!"


# Send message
client = Client(tw_account_sid, tw_auth_token)
message = client.messages \
                .create(
                    body=weather_alert,
                    from_=tw_from_number,
                    to=tw_to_number
                )

print(message.status)
