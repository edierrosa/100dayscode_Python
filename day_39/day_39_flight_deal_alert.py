from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager


# Create instances
data_manager = DataManager()
sheety_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()


# Update destination code
if sheety_data[0]["iataCode"] == "":
    for _ in sheety_data:
        _["iataCode"] = flight_search.get_destination_code(_["city"])
    print(f"sheety_data:\n {sheety_data}")
    data_manager.destination_data = sheety_data
    data_manager.update_destination_codes()


# Get today's and six months' date
tomorrow = datetime.now() + timedelta(days=1)
six_months_date = datetime.now() + timedelta(days=180)


# Check for low price flight and send SMS
for _ in sheety_data:
    flight = flight_search.check_flights(
        "LON",
        _["iataCode"],
        from_time=tomorrow,
        to_time=six_months_date
    )
    try:
        if flight.price <= _["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date} for £{flight.price}.")
    except AttributeError:
        pass
