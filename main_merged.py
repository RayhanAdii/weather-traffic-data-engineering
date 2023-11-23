import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
import logging

def extract_traffic():
    api_url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/relative/10/json?key=GyrwSRUHGsEJP9wCFTGyvWx2LSCGaOtN&point=-7.761175,110.380499" 
    response = requests.get(api_url)


    if response.status_code == 200:
        data = response.json()
        df_traffic = pd.DataFrame(data["flowSegmentData"])
    else:
        print("Failed to fetch traffic data from the API.")
    
    return df_traffic

def extract_weather():

    api_url = "https://api.open-meteo.com/v1/forecast?latitude=-7.761175&longitude=110.380499&current=temperature_2m,relative_humidity_2m,precipitation,rain,showers,wind_speed_10m" 
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json() 
        df_weather = pd.DataFrame(data)
    else:
        print("Failed to fetch weather data from the API.")

    return df_weather

def transform_traffic(df_traffic):
    #Transform DF traffic

    # Reset Index
    df_traffic = df_traffic.reset_index()

    #S elect Only needed column
    df_traffic = df_traffic.loc[:,["currentSpeed","freeFlowSpeed","confidence","roadClosure"]]

    # Add Timestamp
    df_traffic['Time'] = datetime.now().strftime('%Y-%m-%d %H:%M')

    # Rename Column
    df_traffic.rename(columns={ 'currentSpeed': 'current_speed',
                                'freeFlowSpeed': 'free_flow_speed',
                                'confidence': 'confidence',
                                'roadClosure': 'road_closure',
                                'Time': 'traffic_timestamp'},
                                inplace=True)

    return df_traffic

def transform_weather(df_weather):
    #Transform DF Weather

    #Get needed value only
    df_weather = df_weather[["current"]]

    #Transpose and Reset Index
    df_weather = df_weather.transpose().reset_index()

    #Select Only needed column
    df_weather = df_weather.loc[:,["time","precipitation","temperature_2m","wind_speed_10m","rain","showers","relative_humidity_2m"]]

    #Datatype Casting
    df_weather['time'] = pd.to_datetime(df_weather['time'])
    df_weather["precipitation"] = df_weather["precipitation"].astype(float)
    df_weather["temperature_2m"] = df_weather["temperature_2m"].astype(float)
    df_weather["wind_speed_10m"] = df_weather["wind_speed_10m"].astype(float)
    df_weather["rain"] = df_weather["rain"].astype(float)
    df_weather["showers"] = df_weather["showers"].astype(float)
    df_weather["relative_humidity_2m"] = df_weather["relative_humidity_2m"].astype(float)
    df_weather["rain"] = df_weather["rain"].astype(float)

    # Add 7 hours into datetime column so that it become GMT+7, then set into desired format
    hours_to_add = pd.to_timedelta('7 hours')
    df_weather['time'] = df_weather['time'] + hours_to_add
    df_weather['time'] = df_weather['time'].dt.strftime('%Y-%m-%d %H:%M')

    # Rename Column
    df_weather.rename(columns={'time': 'weather_timestamp'},inplace=True)

    return df_weather

def extract():
    df_traffic = extract_traffic()
    df_weather = extract_weather()
    return df_traffic, df_weather

def transform(df_traffic, df_weather):
    
    df_traffic = transform_traffic(df_traffic)
    df_weather = transform_weather(df_weather)

    return df_traffic, df_weather

def load(df_traffic, df_weather):

    engine = create_engine('postgresql://rekdatkelompoka:rekdata@34.31.99.117/traffic-weather')
    #engine = create_engine('postgresql://spkfqrtx:RbQ0GfHW5OXX3KRxfNKGdA8JO0d2njzh@bubble.db.elephantsql.com/spkfqrtx')
    
    df_traffic.to_sql('traffic', engine, if_exists='append', index=False)
    df_weather.to_sql('weather', engine, if_exists='append', index=False)
    print(f"ETL Success at {datetime.now()}")

#Extract
df_traffic, df_weather = extract()

#Transform
df_traffic, df_weather = transform(df_traffic, df_weather)

#Load
load(df_traffic,df_weather)
