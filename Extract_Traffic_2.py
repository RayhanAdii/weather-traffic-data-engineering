import requests
import pandas as pd
import json

api_url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/relative/10/json?key=GyrwSRUHGsEJP9wCFTGyvWx2LSCGaOtN&point=-7.761175,110.380499"  # Replace with the API URL you want to fetch data from
response = requests.get(api_url)


if response.status_code == 200:
    #print(response.json())
    data = response.json()  # Assuming the API returns JSON data\
    #df = pd.json_normalize(data, 'flowSegmentData.coordinates.coordinate')
    #data = json.loads(data)
    #coordinates_data = data["coordinates"]
    #df = pd.DataFrame(data)
else:
    print("Failed to fetch data from the API.")

print(data)