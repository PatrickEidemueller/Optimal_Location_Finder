from math import cos, asin, sqrt, pi
import pandas as pd


# Berechne Distanz nach Haversine Formel
def dist(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

# Lat und Lon von Restaurant
lat=9.0516854
lon= 76.5360752


# Stations einlesen
stations = pd.read_csv("data/stations.csv", sep=";")
stations = stations[['id', 'latitude', 'longitude']]

# Berechne Distanzen
stations['dist'] = stations.apply(lambda row: dist(row['latitude'], row['longitude'],lat, lon), axis=1)

# Suche Station mit minimaler Distanz
station_closest = stations[stations['dist'] == min(stations['dist'])]
station_closest_id = station_closest[['id','dist']]
print(station_closest_id)

