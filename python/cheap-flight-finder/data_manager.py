import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.getlink = "YOUR SHEETY API LINK"
        self.getlink_users = "YOUR SHEETY API LINK"
        self.postlink_price = "YOUR SHEETY API LINK"
        self.postlink_users = "YOUR SHEETY API LINK"
        self.putlink_incomplete = "YOUR SHEETY API LINK"

    def get_data_price(self):
        response = requests.get(url=self.getlink)
        return response.json()
    
    def get_data_users(self):
        response = requests.get(url=self.getlink_users)
        return response.json()['users']
    
    def put_iataCode(self, city_code: list[dict]):
        for data in city_code:
            data_to_put = {
                'price': {
                    'iataCode': data["city"]
                }
            }
            response = requests.put(url=f"{self.putlink_incomplete}/{data['row']}", json=data_to_put)
            response.raise_for_status()
    
    def post_customer_data(self, first_name: str, last_name: str, email: str):
        config = {
            'user':{
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
        }
        response = requests.post(url=self.postlink_users, json=config)
        response.raise_for_status()