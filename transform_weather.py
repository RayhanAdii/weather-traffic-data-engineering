import pandas as pd

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