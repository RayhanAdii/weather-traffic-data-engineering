import requests
import pandas as pd

def extract_traffic():
    api_url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/relative/10/json?key=GyrwSRUHGsEJP9wCFTGyvWx2LSCGaOtN&point=-7.761175,110.380499" 
    response = requests.get(api_url)


    if response.status_code == 200:
        data = response.json()
        df_traffic = pd.DataFrame(data["flowSegmentData"])
    else:
        print("Failed to fetch traffic data from the API.")
    
    return df_traffic

