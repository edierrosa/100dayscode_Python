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
            url=f"{sheety_endpoint}prices", headers=sheety_headers)
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

    def get_customer_emails(self):
        sheety_get_request = requests.get(
            url=f"{sheety_endpoint}users", headers=sheety_headers)
        self.customer_data = sheety_get_request.json()["users"]
        return self.customer_data

    def user_sign_up(self):
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        user_email = input("Your Email: ")
        confirmed_email = input("Please, confirm your email: ")

        while user_email != confirmed_email:
            print("Email does not match. Please, type again.")
            user_email = input("Your Email: ")
            confirmed_email = input("Please, confirm your email: ")

        user_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": confirmed_email
            }
        }
        sheety_post_request = requests.post(
            url=f"{sheety_endpoint}/users", json=user_data, headers=sheety_headers)
        print(sheety_post_request.text)
