from dotenv import load_dotenv
import os
from unittest import result
from urllib import response
import requests 
import json

load_dotenv()
key = os.getenv('METOFFICE_KEY')

weather_obs_api = 'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/3354?res=hourly&key='+key

def getWeatherType(type):
    weatherDict = {
        "NA" : "Not available",
        "0" : "Clear night",
        "1" : "Sunny day",
        "2" : "Partly cloudy (night)",
        "3" : "Partly cloudy (day)",
        "4" : "Not used",
        "5" : "Mist",
        "6" : "Fog",
        "7" : "Cloudy",
        "8" : "Overcast",
        "9" : "Light rain shower (night)",
        "10" : "Light rain shower (day)",
        "11" : "Drizzle",
        "12" : "Light rain",
        "13" : "Heavy rain shower (night)",
        "14" : "Heavy rain shower (day)",
        "15" : "Heavy rain",
        "16" : "Sleet shower (night)",
        "17" : "Sleet shower (day)",
        "18" : "Sleet",
        "19" : "Hail shower (night)",
        "20" : "Hail shower (day)",
        "21" : "Hail",
        "22" : "Light snow shower (night)",
        "23" : "Light snow shower (day)",
        "24" : "Light snow",
        "25" : "Heavy snow shower (night)",
        "26" : "Heavy snow shower (day)",
        "27" : "Heavy snow",
        "28" : "Thunder shower (night)",
        "29" : "Thunder shower (day)",
        "30" : "Thunder"}
    return(weatherDict[type])

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
            if int(ob['$']) == (int(current_hour)-1) * 60: # Need to -1 hour as latest observation is from previous hour
                print(ob)
                print(f'Temprature: {ob["T"]} degC')
                print(f'Visability: {ob["V"]} m')
                print(f'Wind Direction: {ob["D"]}')
                print(f'Wind Speed: {ob["S"]} mph')
                print(f'Wind Gust: {ob["G"]} mph')
                print(f'Weather Type: {getWeatherType(ob["W"])}')
                print(f'Pressure: {ob["P"]} hpa (mBar)')
                print(f'Pressure Trend: {ob["Pt"]}')
                print(f'Dew Point: {ob["Dp"]} degC')
                print(f'Relative Humidity: {ob["H"]} %')
