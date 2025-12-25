# Weather App (Python)
# Oasis Infobyte Python Development Internship
# Author: Nandini Gaikwad

import requests

API_KEY = "9c59b345e45d1a11e90f83bed39112d3"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print("\nWeather Information")
    print("-------------------")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather}")

else:
    print("City not found. Please check the city name.")
