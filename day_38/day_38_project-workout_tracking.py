from pathlib import Path
import dotenv
import os
import requests
import datetime


# Environment variables
dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)

# Nutrition variables
nutrition_ex_endpoint = os.environ["NUTRITION_EX_ENDPOINT"]
nutrition_headers = {
    "x-app-id": os.environ["NUTRITION_APP_ID"],
    "x-app-key": os.environ["NUTRITION_APP_KEY"],
}

text_input = input("Which exercises did you do today? ")

nutrition_params = {
    "query": text_input,
    "gender": "male",
    "weight_kg": "your weight",
    "height_cm": "your height",
    "age": "your age",
}


# Nutrition exercise post request
nutrition_ex_response = requests.post(
    nutrition_ex_endpoint, json=nutrition_params, headers=nutrition_headers)
nutrition_ex_data = nutrition_ex_response.json()["exercises"]
# print(nutrition_ex_data)


# Date
today_date = datetime.datetime.now().strftime("%d/%m/%Y")
time_now = datetime.datetime.now().strftime("%X")


# Sheety variables
sheety_get_endpoint = os.environ["SHEETY_GET_END"]
sheety_post_endpoint = os.environ["SHEETY_POST_END"]
sheety_headers = {
    "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
}


# Sheety post request
def sheety_post(sheety_json):
    sheety_ex_post = requests.post(
        sheety_post_endpoint, json=sheety_json, headers=sheety_headers)
    print(sheety_ex_post.text)


for exercise in nutrition_ex_data:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_post(sheety_params)
