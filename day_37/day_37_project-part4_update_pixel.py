import datetime
import requests
import dotenv
from pathlib import Path
import os


# Environment variables
dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)

today = datetime.datetime.now()
pixel_date = today.strftime("%Y%m%d")

# Pixela variables
pixela_endpoint = f'{os.environ["PIXELA_GRAPHS_ENDPOINT"]}/graph1/{pixel_date}'

pixela_headers = {
    "X-USER-TOKEN": os.environ["PIXELA_USER_TOKEN"],
}

pixela_update_pixel = {
    "quantity": "30",
}

new_pixela_put_request = requests.put(
    url=pixela_endpoint, json=pixela_update_pixel, headers=pixela_headers)
print(new_pixela_put_request.json, new_pixela_put_request.text)
