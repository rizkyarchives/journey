import requests
from datetime import date, timedelta
API_KEY = "YOUR TEQUILA API KEY"
FLY_FROM = "LON" #Just for testing purposes

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.locations_link = 'https://api.tequila.kiwi.com/locations/query'
        self.search_link = 'https://api.tequila.kiwi.com/v2/search'
        self.header = {
            'apikey': API_KEY,
        }
        self.current_date = date.today()
        self.tomorrow = (self.current_date + timedelta(days=1)).strftime("%d/%m/%Y")
        self.six_months_later = (self.current_date + timedelta(days=6*30)).strftime("%d/%m/%Y")

    def search_iataCode(self, missing_code_data: list):
        for index, city in enumerate(missing_code_data):
            config = {
                'term': city['city'],
                'location_types': 'city'
            }
            response = requests.get(url=self.locations_link, headers=self.header, params=config)
            response.raise_for_status()
            data = response.json()
            missing_code_data[index]['city'] = data['locations'][0]['code']
        return missing_code_data

    def search_prices(self, price_to_search: list[dict]):
        for index, data in enumerate(price_to_search):
            config = {
                'fly_from': FLY_FROM,
                'fly_to': data['iataCode'],
                'date_from': self.tomorrow,
                'date_to': self.six_months_later,
                'only_working_days': False,
                'only_weekends': False,
                'partner_market': 'us',
                'price_to': int(data['lowestPrice']),
                'vehicle_type': 'aircraft',
                'limit': 1,
                'curr': 'USD'
            }
            response = requests.get(url=self.search_link, headers=self.header, params=config)
            response.raise_for_status()
            results = response.json()
            if results["_results"] > 0:
                price_to_search[index].update({'worth_buying': True, 
                                               'price': results['data'][0]['price'], 
                                               'date_from': self.tomorrow, 
                                               'date_to': self.six_months_later,
                                               'fly_from': f"{results['data'][0]['flyFrom']}-{results['data'][0]['cityFrom']}",
                                               'fly_to': f"{results['data'][0]['flyTo']}-{results['data'][0]['cityTo']}",
                                               'link': results['data'][0]['deep_link']
                                               })
            else:
                price_to_search[index].update({'worth_buying': False})

            
        return price_to_search
