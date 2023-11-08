from extract import extract
from transform import transform
import pandas as pd

#Extract
df_traffic, df_weather = extract()

#Transform
df_traffic, df_weather = transform(df_traffic, df_weather)



print(df_weather)
print(df_traffic)
