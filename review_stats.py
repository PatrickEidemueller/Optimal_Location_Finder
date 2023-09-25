import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
data_file = open("data/yelp_academic_dataset_review.json")
data = []
for line in data_file:
    data.append(json.loads(line))
review_df = pd.DataFrame(data)
data_file.close()

print(review_df.head())
print(review_df.info())
print(review_df.describe())
stars = review_df['stars']

stars.hist(grid=False)
plt.savefig("reviewstarshist.png")
