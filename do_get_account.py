import json
import requests
import bs4 as bs

api_token = 'your_api_token'
api_url_base = 'https://api.openei.org/utility_rates?version=latest&format=json&sector=Residential&api_key=0qhns3LUhrH21EdMOuSP1I7GFsL3EkkmPak6X1PU&ratesforutility=Detroit Edison Co'

r = requests.get(url = api_url_base)

data = r.json()

print(data)

keep = data['items'][0]["uri"]


rates = requests.get(keep)

soup = bs.BeautifulSoup(rates.text, 'html.parser')

