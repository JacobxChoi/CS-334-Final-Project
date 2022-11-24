import pandas as pd

business_json_path = 'yelp_dataset/yelp_academic_dataset_business.json'
data = pd.read_json(business_json_path, lines=True)
#print("data: ", data.shape)
restaurant = data.dropna(subset=['categories'])
#print("any null?: ", restaurant['categories'].isnull().values.any())
restaurant = restaurant[restaurant['categories'].str.contains("Restaurants")]

restaurant.to_csv("restaurant_businesses.csv")
