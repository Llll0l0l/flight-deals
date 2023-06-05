import requests

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, iata, id) -> None:
        self.id = id
        self.iata = iata
        self.url = f"https://api.sheety.co/446e0bfe88c9e058230f083f6e7edeee/copyOfFlightDeals/prices/{self.id}"
        self.update_iata()

    def update_iata(self) -> None:
        try:
            payload = {
                "price": {
                    "iataCode": self.iata
                }
            }
            response = requests.put(url=self.url, json=payload)
            response.raise_for_status()
            print("IATA code updated successfully!")
        except requests.exceptions.RequestException as e:
            print("Error updating IATA code:", e)
