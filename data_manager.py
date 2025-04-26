# handles the interaction between the Google Sheets

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
from dotenv import load_dotenv 
import os

# Loading all of the environmental variables within our .env file.
load_dotenv() 

FLIGHT_URL = 'https://api.sheety.co/9a5f2f38c579638928123fbfa4eab617/flightDeals/prices'

class Data_Manager:

    # inititalization function
    def __init__(self):
        self.username = os.environ.get('USERNAME')
        self.password = os.environ.get('PASSWORD') 
        self.auth = HTTPBasicAuth(self.username, self.password)
        # self.token = os.environ.get('BEARER_TOKEN') # if we use the BEARER method of auth.
        self.flight_data = {}

    def get_sheet_data(self):

        # if we use the BEARER method of auth.
        # headers = { 
        #     'Authorization': f'Bearer {self.token}'
        # }

        f_response = requests.get(url=FLIGHT_URL, 
                                auth= self.auth,
        )
        data = f_response.json()
        self.flight_data = data['prices']
        # pprint(sheet_data)
        return self.flight_data

