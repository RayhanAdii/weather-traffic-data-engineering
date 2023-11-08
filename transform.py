from transform_traffic import transform_traffic
from transform_weather import transform_weather

def transform(df_traffic, df_weather):
    
    df_traffic = transform_traffic(df_traffic)
    df_weather = transform_weather(df_weather)

    return df_traffic, df_weather