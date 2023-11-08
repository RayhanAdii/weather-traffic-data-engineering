from sqlalchemy import create_engine
import pandas as pd
import logging

def load(df_traffic, df_weather):

    engine = create_engine('postgresql://rekdatkelompoka:rekdata@localhost/traffic-weather')
    df_traffic.to_sql('traffic', engine, if_exists='append', index=False)
    df_weather.to_sql('weather', engine, if_exists='append', index=False)
    print("ETL Success")

