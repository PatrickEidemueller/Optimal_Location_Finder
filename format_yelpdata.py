import pandas as pd
import numpy as np
import json

data_file = open("data/yelp_academic_dataset_business.json")
data = []
for line in data_file:
    data.append(json.loads(line))
restaurant_df = pd.DataFrame(data)
data_file.close()

restaurant_df.drop(columns =['hours', 'attributes'], inplace =True)
#restaurant_df = restaurant_df[restaurant_df['is_open']==1]

restaurant_df = restaurant_df[restaurant_df.categories.str.contains("Restaurant")==True]

print(restaurant_df.shape)

print(restaurant_df.head)

restaurant_df.to_json("data/yelp_academic_dataset_business_format.json", orient = 'records')