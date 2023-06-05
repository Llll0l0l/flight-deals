import requests
from flight_search import FlightSearch
from data_manager import DataManager
from pprint import pprint

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

flight_deals_endpoint = "https://api.sheety.co/446e0bfe88c9e058230f083f6e7edeee/copyOfFlightDeals/prices"

response = requests.get(url=flight_deals_endpoint)

# prices
sheet_data = response.json()["prices"]

for data in sheet_data:
    
    city = data["city"]

    # get the iata code from flight_Search
    test = FlightSearch(city)
    iata = test.return_iata()
    # fill the sheet_data with iata
    data["iataCode"] = iata
    pprint(data)
    # fill the google sheet with iata
    data_mng = DataManager(data["iataCode"], data["id"])