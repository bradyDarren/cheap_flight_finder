from data_manager import Data_Manager
from pprint import pprint
from flight_search import FlightSearch
import time

test = Data_Manager()
sheet = test.get_sheet_data()

# pprint(sheet)

search = FlightSearch()

# for row in sheet: 
#     if row['iataCode'] == '':
#         row['iataCode'] = search.get_iatacode(row['city'])
#         time.sleep(2)

# test.flight_data = sheet
# test.change_iataCode()

pprint(search.search()['data'][0]['price']['grandTotal'])