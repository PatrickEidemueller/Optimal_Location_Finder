# load relevant packages

from math import cos, asin, sqrt, pi
import pandas as pd
import numpy as np
import json
import sqlalchemy
import psycopg2

"""
Calculate the great circle distance between two points
on the earth (specified in decimal degrees)
All args must be of equal length.
"""


def haversine_np(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2.0) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0) ** 2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km


# Business json einlesen
def read_business_json(path):
    data_file = open(path)
    data = []
    for line in data_file:
        data.append(json.loads(line))
    restaurant_df = pd.DataFrame(data)
    data_file.close()
    return restaurant_df


# stations einlesen
def read_station_csv():
    stations = pd.read_csv("/home/sync/weather/stations.csv", sep=";")
    # create df with only necessary columns
    stations = stations[['id', 'latitude', 'longitude', 'state']]
    return stations


def filter_business(df):
    # filter for only restaurants
    restaurant_df = df[df.categories.str.contains("Restaurant") == True]
    # filter for only open restaurants
    #restaurant_df = restaurant_df[restaurant_df['is_open'] == 1]
    # filter for flawed location data
    restaurant_df.drop(restaurant_df[restaurant_df.longitude > 0].index, inplace=True)
    restaurant_df.drop(columns=['hours', 'attributes'], inplace=True)

    return restaurant_df

