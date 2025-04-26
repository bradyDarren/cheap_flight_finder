# handles the interaction between the Google Sheets

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv 
import os

class Data_Manager:

    def __init__(self):
        self.username = os.environ()
        self.password = os.environ() 
        self.auth = HTTPBasicAuth(self.username, self.password)
        self.flight_data = {}

    def get_sheet_data(self):

FLIGHT_URL = 'https://api.sheety.co/9a5f2f38c579638928123fbfa4eab617/flightDeals/prices'


f_response = requests.get(url=FLIGHT_URL, 
                          auth= HTTPBasicAuth(USERNAME, PASSWORD)
)
pprint(f_response.json())