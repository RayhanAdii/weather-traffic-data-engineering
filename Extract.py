import json
import requests
import pandas as pd

def extract():
    # Fetch Weather Data from API
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=-7.761175&longitude=110.380499&past_days=10&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"  # Replace with the API URL you want to fetch data from
    response = requests.get(api_url)

    if response.status_code == 200:
        data_weather = response.json()  # Assuming the API returns JSON data
        df_weather = pd.DataFrame(data_weather)
    else:
        print("Failed to fetch Weather data from the API.")
    
    #

extract()