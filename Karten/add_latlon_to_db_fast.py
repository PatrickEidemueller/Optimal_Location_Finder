import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy
import pgeocode


conn = psycopg2.connect(database="db_sync", user="kevin", password="12345678")
cur = conn.cursor()
def sql(sql: str):
    return pd.read_sql(sql, conn)



edf = sql("SELECT * FROM socio;")
data = pd.read_csv('US.txt', sep="\t", header = None, names=['country','postal', 'name','state' , 'admincode1', 'adminname2', 'admincode2', 'adminname3', 'admincode3','latitude', 'longitude', 'accuracy'])

edf = pd.merge(edf,data[['postal','latitude', 'longitude']],on='postal').drop(columns= ['latitude_x', 'longitude_x'])
edf = edf.rename(columns={"latitude_y": "latitude", "longitude_y": "longitude"})


engine = sqlalchemy.create_engine('postgresql://kevin:12345678@127.0.0.1:5432/db_sync')
edf.to_sql('socio', engine, if_exists='replace', index = False)