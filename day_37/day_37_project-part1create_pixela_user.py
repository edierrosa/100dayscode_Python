import requests
import dotenv
from pathlib import Path
import os


# Environment variables
dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)


# Pixela user variables
pixela_endpoint = os.environ["PIXELA_USERS_ENDPOINT"]
pixela_user_params = {
    "token": os.environ["PIXELA_USER_TOKEN"],
    "username": os.environ["PIXELA_USERNAME"],
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

user_request = requests.post(url=pixela_endpoint, json=pixela_user_params)
print(user_request.json, user_request.text)
