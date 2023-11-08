import pandas as pd
from datetime import datetime

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