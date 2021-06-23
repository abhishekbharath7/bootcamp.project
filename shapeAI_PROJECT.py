import requests
from datetime import datetime

api_key = '976668f8e93832ce56248a6f0a1efdd5'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
file = open("results.txt", "w")

file.write("\n")
file.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))

file.write("\n")
file.write("Current temperature is: {:.2f} deg C".format(temp_city))

file.write("\n")
file.write("Current weather desc  :" + str(weather_desc))

file.write("\n")
file.write("Current Humidity      :" + str(hmdt) + "%")

file.write("\n")
file.write("Current wind speed    :" + str(wind_spd) + "kmph")

file.close()