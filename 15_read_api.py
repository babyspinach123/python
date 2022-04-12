from dotenv import load_dotenv
import os
from unittest import result
from urllib import response
import requests 
import json

load_dotenv()
key = os.getenv('METOFFICE_KEY')

weather_obs_api = 'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/3354?res=hourly&key='+key

response = requests.get(weather_obs_api)
results = response.json()
print('\n----- response ------\n')
print(response)
print('\n----- results ------\n')
print(results)
print('\n-------- json.dumps(results) -------\n')
print(json.dumps(results))

print("\n-------- results['SiteRep']['Wx']['Param'] -------\n")
params = results['SiteRep']['Wx']['Param']
for parameter in params:
    print(parameter)

print("\n-------- Data Date -------\n")
data_date = results['SiteRep']['DV']['dataDate']
print (data_date)
print(data_date.split('T')[0]+'Z')
