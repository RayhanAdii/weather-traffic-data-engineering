from sqlalchemy import create_engine
import pandas as pd
import logging

def load(df_traffic, df_weather):

    engine = create_engine('postgresql://rekdatkelompoka:rekdata@34.121.118.139/traffic-weather')
    #engine = create_engine('postgresql://spkfqrtx:RbQ0GfHW5OXX3KRxfNKGdA8JO0d2njzh@bubble.db.elephantsql.com/spkfqrtx')
    
    df_traffic.to_sql('traffic', engine, if_exists='append', index=False)
    df_weather.to_sql('weather', engine, if_exists='append', index=False)
    print("ETL Success")

