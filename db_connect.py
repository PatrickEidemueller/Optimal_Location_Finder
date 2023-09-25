import psycopg2
import pandas as pd

conn = psycopg2.connect(database="", user="", password="")
#print(conn.closed)
#print(conn.get_dsn_parameters(), "\n")

def print_table(tname: str):
    with conn:
        with conn.cursor() as cur:
            cur.execute('select * from {} limit 10;'.format(tname))
            print(cur.fetchall())

def load_table_station():
    stations = pd.read_csv("../weather/stations.csv", sep=';')
    with conn:
        with conn.cursor() as cur:
            columns = list(stations.columns)
            for i in range(len(stations)):
                values = [stations[column][i] for column in columns]
                cur.execute('insert into station(id, latitude, longitude, elevation, state, name) values(%s, %s, %s, %s, %s, %s);', values)


def delete_entries_table(tname: str):
    with conn:
        with conn.cursor() as cur:
            cur.execute('delete from {};'.format(tname))

print_table("station")
delete_entries_table("station")
print_table("station")
load_table_station()
print_table("station")

conn.close()


