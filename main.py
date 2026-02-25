import os
import requests
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def get_weather(lat, lon, timezone_name):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current_weather=true&timezone={timezone_name}"
    )
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["current_weather"]


def print_weather(city, lat, lon, tz):
    weather = get_weather(lat, lon, tz)

    temp = weather["temperature"]
    windspeed = weather["windspeed"]
    weathercode = weather["weathercode"]
    api_time = weather["time"]

    print(f"\nWeather in {city} at {api_time}:")
    print(f"Temperature: {temp}°C")
    print(f"Wind Speed: {windspeed} km/h")
    print(f"Weather Code: {weathercode}")


def main():
    # CI Runner time (UTC)
    ci_time = datetime.now(timezone.utc)

    # Local times
    erlangen_time = datetime.now(ZoneInfo("Europe/Berlin"))
    zurich_time = datetime.now(ZoneInfo("Europe/Zurich"))

    print("===================================")
    print("CI Run Time (UTC):", ci_time.isoformat())
    print("Local Time Erlangen:", erlangen_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Local Time Zürich:", zurich_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("===================================")

    locations = [
        ("Erlangen", 49.5897, 11.0110, "Europe/Berlin"),
        ("Zürich", 47.3769, 8.5417, "Europe/Zurich"),
    ]

    for city, lat, lon, tz in locations:
        print_weather(city, lat, lon, tz)


if __name__ == "__main__":
    main()