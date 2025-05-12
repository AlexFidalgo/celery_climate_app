import requests
import time
import random

def fetch_weather_data(lat, lon, variables):
    """
    Fetch specified weather variables for a given lat/lon from Open-Meteo.
    """
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": ','.join(variables),
        "forecast_days": 1,
        "timezone": "auto"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()

def fetch_temperature(lat, lon):
    time.sleep(20*random.random())
    return fetch_weather_data(lat, lon, ["temperature_2m"])

def fetch_humidity(lat, lon):
    time.sleep(10*random.random())
    return fetch_weather_data(lat, lon, ["relative_humidity_2m"])
