import requests
import pandas as pd

api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=precipitation,temperature_2m,wind_speed_10m"  # Replace with the API URL you want to fetch data from
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()  # Assuming the API returns JSON data
    df = pd.DataFrame(data)
else:
    print("Failed to fetch data from the API.")



print(df)