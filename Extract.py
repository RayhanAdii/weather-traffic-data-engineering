import requests
import pandas as pd
from Extract_Traffic import extract_traffic
from Extract_Weather import extract_weather

def extract():
    df_traffic = extract_traffic()
    df_weather = extract_weather()
    return df_traffic, df_weather

extract()