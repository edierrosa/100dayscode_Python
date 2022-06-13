import requests
import os
import dotenv
from pathlib import Path
from flight_data import FlightData

dotenv_path = Path(
    "path to .env")
dotenv.load_dotenv(dotenv_path=dotenv_path)

# Environment variables
tequila_location_endpoint = f"{os.environ['TEQUILAKIWI_ENDPOINT']}"
tequila_id = os.environ["TEQUILAKIWI_ID"]
tequila_headers = {
    "apikey": os.environ["TEQUILAKIWI_KEY"]
}


class FlightSearch:
    """This class is responsible for talking to the Flight Search API"""

    def get_destination_code(self, city_name):
        query = {
            "term": city_name,
            "location_types": "city"
        }
        tequila_get_request = requests.get(
            url=f"{tequila_location_endpoint}/locations/query", headers=tequila_headers, params=query)
        tequila_code = tequila_get_request.json()["locations"][0]["code"]
        return tequila_code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_time": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        tequila_check_request = requests.get(
            url=f"{tequila_location_endpoint}/v2/search", headers=tequila_headers, params=query)

        try:
            tequila_check_data = tequila_check_request.json()["data"][0]
        except IndexError:
            try:
                query["max_stopovers"] = 1
                tequila_check_request = requests.get(
                    url=f"{tequila_location_endpoint}/v2/search", headers=tequila_headers, params=query)
                tequila_check_data = tequila_check_request.json()["data"][0]
                flight_data = FlightData(
                    price=tequila_check_data["price"],
                    origin_city=tequila_check_data["route"][0]["cityFrom"],
                    origin_airport=tequila_check_data["route"][0]["flyFrom"],
                    destination_city=tequila_check_data["route"][0]["cityTo"],
                    destination_airport=tequila_check_data["route"][0]["flyTo"],
                    out_date=tequila_check_data["route"][0]["local_departure"].split("T")[
                        0],
                    return_date=tequila_check_data["route"][1]["local_departure"].split("T")[
                        0],
                    stop_overs=1,
                    via_city=tequila_check_data["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city}: £{flight_data.price}")
                return flight_data
            except IndexError:
                print(f"No flights found for {destination_city_code}.")
                return None
        else:
            flight_data = FlightData(
                price=tequila_check_data["price"],
                origin_city=tequila_check_data["route"][0]["cityFrom"],
                origin_airport=tequila_check_data["route"][0]["flyFrom"],
                destination_city=tequila_check_data["route"][0]["cityTo"],
                destination_airport=tequila_check_data["route"][0]["flyTo"],
                out_date=tequila_check_data["route"][0]["local_departure"].split("T")[
                    0],
                return_date=tequila_check_data["route"][1]["local_departure"].split("T")[
                    0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
