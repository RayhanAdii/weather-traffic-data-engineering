from extract import extract
import pandas as pd

#Extract
df_weather, df_traffic = extract()

#Transform DF Weather

#Get needed value only
df_weather = df_weather[["current"]]

#Transform and Reset Index
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


print(df_weather)
print(df_traffic)
