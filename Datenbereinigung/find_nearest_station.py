import business
import pandas as pd
import sqlalchemy
import json


def main():
    #restaurant_df = business.read_business_json()
    engine = sqlalchemy.create_engine('postgresql://kevin:12345678@127.0.0.1:5432/db_sync')
    for c in ['a','b','c','d']:
        restaurant_df = business.read_business_json("/home/sync/yelp/business"+c)
        stations = business.read_station_csv()
        restaurant_df = business.filter_business(restaurant_df)
        alldata = restaurant_df.merge(stations, left_on='state', right_on='state').drop(['categories'], axis=1)
        alldata['distance'] = business.haversine_np(alldata['latitude_x'], alldata['longitude_x'],
                                           alldata['latitude_y'], alldata['longitude_y'])
        nearest_list = (alldata.sort_values(by=["distance"],
                                            ascending=[True]).groupby('business_id', as_index=False, sort=False))
        del alldata

        # create first, second & third nearest
        a = nearest_list.nth(0).drop(['latitude_y', 'longitude_y'], axis=1)
        b = nearest_list.nth(1).drop(['latitude_y', 'longitude_y'], axis=1)
        c = nearest_list.nth(2).drop(['latitude_y', 'longitude_y'], axis=1)

        # rename columns to match column name of db
        a = a.rename(columns={"postal_code": "postal", "latitude_x": "latitude", "longitude_x": "longitude",
                              "distance": "distance_first", "id": "id_first"})
        b = b.rename(columns={"postal_code": "postal", "latitude_x": "latitude", "longitude_x": "longitude",
                              "distance": "distance_second", "id": "id_second"})
        c = c.rename(columns={"postal_code": "postal", "latitude_x": "latitude", "longitude_x": "longitude",
                              "distance": "distance_third", "id": "id_third"})

        #merge a & b
        merged_df = pd.merge(a, b, on=["business_id", "name", "address", "city", "state", "postal", "latitude",
                                   "longitude", "stars", "review_count", "is_open"])
        # merge c
        tidy_business = pd.merge(merged_df, c, on=["business_id", "name", "address", "city", "state", "postal",
                                                   "latitude", "longitude", "stars", "review_count", "is_open"])
        tidy_business.to_sql('business', engine, if_exists='append', index=False)

if __name__ == "__main__":
    main()
