import data_manager
import flight_search
import flight_data
import notification_manager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

sheet = data_manager.DataManager()
flight = flight_search.FlightSearch()
data_handler = flight_data.FlightData()
emailer = notification_manager.NotificationManager()

#Making sure all data in sheets are complete
data = sheet.get_data_price()
rows_without_iataCode = data_handler.format_rows_without_iataCode(data)
iataCode_data = flight.search_iataCode(rows_without_iataCode)
sheet.put_iataCode(iataCode_data)

#Fetching data again from sheet to search for flight prices
data = sheet.get_data_price()['prices']
price_data = flight.search_prices(data)

# Prepare + notifying great deals to user
users = sheet.get_data_users()
content_to_send = data_handler.format_data_to_message(price_data)
emailer.send_message(send_to=users, contents=content_to_send)

print('done')
