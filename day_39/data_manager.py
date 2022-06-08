import requests
import os
import dotenv
from pathlib import Path


dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)

# Environment variables
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
sheety_headers = {
    "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
}


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_get_request = requests.get(
            url=sheety_endpoint, headers=sheety_headers)
        self.destination_data = sheety_get_request.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for _ in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": _["iataCode"]
                }
            }
            sheety_put_request = requests.put(
                url=f"{sheety_endpoint}/{_['id']}", json=new_data, headers=sheety_headers)
            print(sheety_put_request.text)
