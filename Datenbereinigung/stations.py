import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import geopandas as gpd
#from shapely.geometry import Point
#from geopandas import GeoDataFrame

# Daten einlesen und in Spalten aufteilen
stations = pd.read_csv("../data/ghcnd-stations.txt", sep="\n", header=None)
stations.columns=['all']
stations['id'] = stations['all'].apply(lambda str: str[0:11])
stations['latitude'] = stations['all'].apply(lambda str: str[12:20])
stations['longitude'] = stations['all'].apply(lambda str: str[21:30])
stations['elevation'] = stations['all'].apply(lambda str: str[31:37])
stations['state'] = stations['all'].apply(lambda str: str[38:40])
stations['name'] = stations['all'].apply(lambda str: str[41:71])
stations = stations.drop(columns=['all'])

# Leerzeichen in allen Spalten entfernen
for i in range(stations.shape[1]):
    stations[stations.columns[i]] = stations[stations.columns[i]].str.strip()

# Datentyp anpassen
stations[['longitude','latitude']] = stations[['longitude','latitude']].astype(float)

# Nach US/CA Stationen filtern
stations_us = stations[(stations['id'].str[0:2]=='US') | (stations['id'].str[0:2]=='CA')]

# Zähle Stationen pro Bundesstaat
count_stations_state = stations_us.groupby('state').agg(count=pd.NamedAgg(column="id", aggfunc="count")).sort_values('count', ascending=False)

print("Anzahl Staitonen: ",stations_us.shape[0])
print(stations_us.head(10))
print(count_stations_state)

# In csv schreiben
stations_us.to_csv('../weather/stations.csv', index=False, sep=';')


# Karte mit geografischer Verteilung der Stationen (weltweit) erstellen
#us = gpd.read_file('data/cb_2018_us_state_500k.shp')
#us = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#geometry = [Point(xy) for xy in zip(stations['longitude'], stations['latitude'])]
#gdf = GeoDataFrame(stations, geometry=geometry)
#gdf.plot(ax=us.plot(figsize=(80, 48)), marker='o', color='red', markersize=0.5);
#plt.show()

