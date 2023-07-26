class FlightData:
    
    def format_rows_without_iataCode(self, data):
        return [{"row": element['id'], "city": element["city"]} for element in data['prices'] if element["iataCode"] == '']
    
    def format_data_to_message(self, data: list):
        return [{"subject": f"Fly to {element['city']} for cheap!", 
                "content": f"Low price alert! Only ${element['price']} to fly from {element['fly_from']} to {element['fly_to']}, from {element['date_from']} to {element['date_to']}. For information on flight details: {element['link']}"}
                for element in data if element['worth_buying']]