
import os
import psycopg2

import pandas as pd
import numpy as np
import sqlalchemy

engine = sqlalchemy.create_engine('')
#import matplotlib.pyplot as plt
#import geopandas as gpd
#from shapely.geometry import Point
#from geopandas import GeoDataFrame

stations = pd.read_csv("../weather/stations.csv", sep=';')
stations = stations.drop(columns = ['name'], axis = 1)
print(stations.head())
# Nach US/CA Stationen filtern
#stations_us = stations[(stations['id'].str[0:2]=='US') | (stations['id'].str[0:2]=='CA')]


    # Connect to an existing database
connection = psycopg2.connect(user="",password="",host=".1",port="",database="")

 # Create a cursor to perform database operations
cursor = connection.cursor()
    # Print PostgreSQL details
print("PostgreSQL server information")
print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
cursor.execute("SELECT * FROM station")
    # Fetch result
#record = cursor.fetchone()
#print("You are connected to - ", record, "\n")
print(cursor.fetchone())

stations.to_sql('station', engine, if_exists='append', index = False)


