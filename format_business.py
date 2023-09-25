from math import cos, asin, sqrt, pi
import pandas as pd
import numpy as np
import json
from tqdm import tqdm
tqdm.pandas()
import sqlalchemy
import psycopg2

engine = sqlalchemy.create_engine('postgresql://kevin:12345678@127.0.0.1:5432/kevin')

def haversine_np(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.

    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km


# Berechne Distanz nach Haversine Formel
def dist(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(a))

def dist2(loc1,loc2):
    p = pi/180
    a = 0.5 - cos((loc2[1]-loc1[1])*p)/2 + cos(loc1[1]*p)*cos(loc2[1]*p) * (1-cos((loc2[2]-loc1[2])*p)) / 2
    return 12742 * asin(sqrt(a))


# Business json einlesen
data_file = open("/home/sync/yelp/yelp_academic_dataset_business.json")
data = []
for line in data_file:
    data.append(json.loads(line))
restaurant_df = pd.DataFrame(data)
data_file.close()

restaurant_df.drop(columns =['hours', 'attributes'], inplace =True)
#restaurant_df = restaurant_df[restaurant_df['is_open']==1]

restaurant_df = restaurant_df[restaurant_df.categories.str.contains("Restaurant")==True]

# Stations einlesen
stations = pd.read_csv("data/stations.csv", sep=";")
stations = stations[['id', 'latitude', 'longitude', 'state']]

alldata = restaurant_df.merge(stations, left_on='state', right_on='state').drop(['categories'],axis = 1)

del stations
del restaurant_df

#distances = restaurant_df[restaurant_df['state'] == 'BC'].progress_apply(lambda rrow: stations[stations['state'] == rrow['state']].apply(lambda srow: dist(srow['latitude'],srow['longitude'], rrow['latitude'], rrow['longitude']), axis = 1), axis = 1)
#distances = restaurant_df.progress_apply(lambda rrow: stations[stations['state'] == rrow['state']].apply(lambda srow: dist(srow['latitude'],srow['longitude'], rrow['latitude'], rrow['longitude']), axis = 1), axis = 1)
alldata['distance'] = haversine_np(alldata['latitude_x'],alldata['longitude_x'],alldata['latitude_y'],alldata['longitude_y'])

nearest_list = (alldata.sort_values(by = ["business_id","distance"], ascending=[True,True]).groupby('business_id', as_index = False, sort = False))
del alldata
a = nearest_list.nth(0).drop(['latitude_y', 'longitude_y'],axis = 1)
b = nearest_list.nth(1).drop(['latitude_y', 'longitude_y'],axis = 1)
c = nearest_list.nth(2).drop(['latitude_y', 'longitude_y'],axis = 1)

a = a.rename(columns={"postal_code": "postal", "latitude_x": "latitude", "longitude_x": "longitude", "distance": "distance_first"})
b = b.rename(columns={"postal_code": "postal", "latitude_x": "latitude", "longitude_x": "longitude", "distance": "distance_second", "id": "sta_id" })
c = c.rename(columns={"postal_code": "postal", "latitude_x": "latitude", "longitude_x": "longitude", "distance": "distance_third", "id": "sta_id2"})

merged_df = pd.merge(a, b, on=["business_id", "name", "address", "city", "state", "postal", "latitude", "longitude", "stars", "review_count", "is_open"])

tidy_business = pd.merge(merged_df, c, on=["business_id", "name", "address", "city", "state", "postal", "latitude", "longitude", "stars", "review_count", "is_open"])

print(a)
print(b)
print(c)

print(tidy_business)

tidy_business.to_sql('business', engine, if_exists='append', index = False)

#for rindex, rrow in restaurant_df.iterrows():
    # Berechne Distanzen
 #   print(rindex)
  #  stations['dist'] = stations.apply(lambda x: dist(x['latitude'], x['longitude'], rrow['latitude'], rrow['longitude']),axis = 1)
    # stations['dist'] = stations.apply(lambda row: dist(row['latitude'], row['longitude'], rrow['latitude'][0], rrow['longitude'][0]),axis=1)
    # Suche Station mit minimaler Distanz
   # closest_index = (stations[['dist']].idxmin())[0]
    #restaurant_df.at[rindex, 'distance_first'] = stations.at[closest_index, 'dist']
    #restaurant_df.at[rindex, 'sta_station_id'] = stations.at[closest_index, 'id']
    #station_closest = stations[stations['dist'] == min(stations['dist'])]
    #station_closest_id = station_closest[['id', 'dist']]

#print(restaurant_df)




