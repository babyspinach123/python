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
# "2022-04-24T14:00:00Z"4
current_date= data_date.split('T')[0]+'Z'
print(current_date)
current_time = data_date.split('T')[1]
current_hour = current_time.split(':')[0]
print(current_time)
print(current_hour)
period = results['SiteRep']['DV']['Location']['Period']
# print(period)

for i in period:
    print(i['value'])
    if i['value'] == current_date:
        # print(i['Rep'])
        for ob in i['Rep']:
            if int(ob['$']) == int(current_hour) * 60:
                print(ob)
                print(f'Temprature: {ob["T"]} degC')
    