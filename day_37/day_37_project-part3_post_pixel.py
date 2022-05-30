import datetime
import requests
import dotenv
from pathlib import Path
import os


# Environment variables
dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)


# Pixela variables
pixela_endpoint = f'{os.environ["PIXELA_GRAPHS_ENDPOINT"]}/graph1'

pixela_headers = {
    "X-USER-TOKEN": os.environ["PIXELA_USER_TOKEN"],
}

today = datetime.now()
pixel_date = today.strftime("%Y%m%d")


pixela_post_pixel = {
    "date": pixel_date,
    "quantity": "10",
}

new_pixela_post_request = requests.post(
    url=pixela_endpoint, json=pixela_post_pixel, headers=pixela_headers)
print(new_pixela_post_request.json, new_pixela_post_request.text)
