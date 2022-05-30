import requests
import dotenv
from pathlib import Path
import os


# Environment variables
dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)

# Pixela variables
pixela_endpoint = f'{os.environ["PIXELA_USERS_ENDPOINT"]}/{os.environ["PIXELA_USERNAME"]}'

pixela_headers = {
    "X-USER-TOKEN": os.environ["PIXELA_USER_TOKEN"],
}

new_pixela_delete_request = requests.delete(
    url=pixela_endpoint, headers=pixela_headers)
print(new_pixela_delete_request.json, new_pixela_delete_request.text)
