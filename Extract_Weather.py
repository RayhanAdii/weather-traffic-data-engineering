import requests
import pandas as pd

def extract_weather():

    api_url = "https://api.open-meteo.com/v1/forecast?latitude=-7.761175&longitude=110.380499&current=temperature_2m,relative_humidity_2m,precipitation,rain,showers,wind_speed_10m" 
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json() 
        df_weather = pd.DataFrame(data)
    else:
        print("Failed to fetch weather data from the API.")

    return df_weather