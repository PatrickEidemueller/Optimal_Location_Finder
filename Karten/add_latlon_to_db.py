import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy
import pgeocode


conn = psycopg2.connect(database="", user="", password="")
cur = conn.cursor()
def sql(sql: str):
    return pd.read_sql(sql, conn)


nomi = pgeocode.Nominatim('us')
edf = sql("SELECT * FROM socio;")

def get_lat(pcode):
    try:
        x = nomi.query_postal_code(pcode).latitude
        return x
    except:
        return np.NaN

def get_long(pcode):
    try:
        x = nomi.query_postal_code(pcode).longitude
        return x
    except:
        return np.NaN
    

edf['latitude'] = np.vectorize(get_lat)(edf['postal'])
edf['longitude'] = np.vectorize(get_long)(edf['postal'])


engine = sqlalchemy.create_engine('postgresql://kevin:12345678@127.0.0.1:5432/db_sync')
edf.to_sql('socio', engine, if_exists='replace', index = False)
