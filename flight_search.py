# # handles the communications to the Flight Search API. 

import requests
import os
from dotenv import load_dotenv

load_dotenv()

CORE_ENDPOINT = 'https://test.api.amadeus.com/v1'
TOKEN_ENDPOINT = '/security/oauth2/token'
CITY_SEARCH_ENDPOINT = '/reference-data/locations/cities'

class FlightSearch: 

    def __init__(self):
        self.api_key = os.environ.get('API_KEY')
        self.api_secret = os.environ.get('API_SECRET')
        self.token = self.get_new_token()

    def get_new_token(self):

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }

        response = requests.post(url=f'{CORE_ENDPOINT}{TOKEN_ENDPOINT}',
                                 headers=headers,
                                 data=body
        )
        token = response.json()['access_token']
        return token

    def get_iatacode(self, city_name):

        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        datas = {
            'keyword': city_name,
        }

        response = requests.get(url=f'{CORE_ENDPOINT}{CITY_SEARCH_ENDPOINT}',
                                headers=headers,
                                params=datas
        )

        try: 
            iatacode = response.json()['data'][0]['iataCode']
        except IndexError: 
            print(f'IndexError: No airport code found for {city_name}')
            return 'N/A'
        except KeyError: 
            print(f'KeyError: No airport code found for {city_name}')
            return 'Not Found'
        
        return iatacode
    
    def search(self):
        


    
