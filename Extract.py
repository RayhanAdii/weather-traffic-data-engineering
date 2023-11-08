from extract_traffic import extract_traffic
from extract_weather import extract_weather

def extract():
    df_traffic = extract_traffic()
    df_weather = extract_weather()
    return df_traffic, df_weather

