from . import app
from .climate_api import fetch_temperature, fetch_humidity

@app.task
def get_temperature(lat, lon):
    return fetch_temperature(lat, lon)

@app.task
def get_humidity(lat, lon):
    return fetch_humidity(lat, lon)
