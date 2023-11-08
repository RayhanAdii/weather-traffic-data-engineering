from extract import extract
from transform import transform
from load import load


#Extract
df_traffic, df_weather = extract()

#Transform
df_traffic, df_weather = transform(df_traffic, df_weather)

#Load
load(df_traffic,df_weather)

