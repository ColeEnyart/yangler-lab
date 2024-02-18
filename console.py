import pandas as pd
import requests


def open_meteo_api():
    url = "https://archive-api.open-meteo.com/v1/era5"
    params = {
        "latitude": 44.9444,
        "longitude": -93.0933,
        "daily": ["temperature_2m_max", "temperature_2m_min"],
        "temperature_unit": "fahrenheit",
        "start_date": "2024-02-10",
        "end_date": "2024-02-11",
    }
    response = requests.get(url, params)
    weather = response.json()
    df = pd.DataFrame(weather)
    return df


def coerce(df):
    date = pd.to_datetime(df["daily"].iloc[0], errors="coerce")
    daily_temperature_2m_max = pd.to_numeric(df["daily"].iloc[1], errors="coerce")
    daily_temperature_2m_min = pd.to_numeric(df["daily"].iloc[2], errors="coerce")

    daily_data = {
        "date": date,
        "max_temp": daily_temperature_2m_max,
        "min_temp": daily_temperature_2m_min,
    }

    return pd.DataFrame(data=daily_data)

response = open_meteo_api()
ans = coerce(response)
