import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
data_file = open("/home/sync/yelp/yelp_academic_dataset_business.json")
data = []
for line in data_file:
    data.append(json.loads(line))
restaurant_df = pd.DataFrame(data)
data_file.close()


us = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
geometry = [Point(xy) for xy in zip(restaurant_df['longitude'], restaurant_df['latitude'])]
gdf = GeoDataFrame(restaurant_df, geometry=geometry)
gdf.plot(ax=us.plot(figsize=(80, 48)), marker='o', color='red', markersize=2.5);
plt.savefig("restaurants2.png")

