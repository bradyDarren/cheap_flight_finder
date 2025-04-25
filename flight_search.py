# handles the communications to the Flight Search API. 

import requests
import os

API_KEY = os.environ.get("APP_KEY")
API_SEC =  os.environ.get("APP_SEC")
TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'

token_headers = { 
    "Content-Type":"application/x-www-form-urlencoded",
}

token_data = { 
    'grant_type':'client_credentials',
    'client_id': API_KEY,
    'client_secret': API_SEC,
}

token = requests.post(url=TOKEN_ENDPOINT, headers=token_headers, data=token_data)
print(token.json())