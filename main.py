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

    # get the iata code for each city
    endpoint_iata = "https://api.tequila.kiwi.com/locations/query"
    
    API_KEY = "YI0eE72GWPacazqUJAktNNxJvXjwoONc"
    params = {
        "term": city,
    }

    headers = {
        "apikey": API_KEY,
    }

    iata_response = requests.get(url=endpoint_iata, headers=headers, params=params)
    iata_response.raise_for_status()
    city_iata = iata_response.json()["locations"][0]["code"]


    # fill the sheet_data with iata
    data["iataCode"] = iata
    # fill the google sheet with iata
    data_mng = DataManager(city_iata, data["id"])