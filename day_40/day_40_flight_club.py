from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Create instances
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheety_data = data_manager.get_destination_data()

# Update destination code
if sheety_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheety_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheety_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheety_data}

# Get today's and six months' date
tomorrow = datetime.now() + timedelta(days=1)
six_months_date = datetime.now() + timedelta(days=180)

for destination_code in destinations:
    flight = flight_search.check_flights(
        "LON",
        destination_code,
        from_time=tomorrow,
        to_time=six_months_date
    )
    if flight is None:
        continue

    if flight.price <= destinations[destination_code]["price"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_mail(emails, message, link)
