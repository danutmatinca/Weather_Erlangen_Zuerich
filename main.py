import os
import requests
from datetime import datetime

def get_weather(lat, lon, timezone):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&timezone={timezone}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['current_weather']

def print_weather(city, lat, lon, tz):
    weather = get_weather(lat, lon, tz)
    temp = weather['temperature']
    windspeed = weather['windspeed']
    weathercode = weather['weathercode']
    time = weather['time']

    print(f"\nWeather in {city} at {time}:")
    print(f"Temperature: {temp}°C")
    print(f"Wind Speed: {windspeed} km/h")
    print(f"Weather Code: {weathercode}")

def main():
    locations = [
        ("Erlangen", 49.5897, 11.0110, "Europe/Berlin"),
        ("Zürich", 47.3769, 8.5417, "Europe/Zurich")
    ]

    for city, lat, lon, tz in locations:
        print_weather(city, lat, lon, tz)

if __name__ == "__main__":
    main()