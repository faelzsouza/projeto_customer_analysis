from IPython.core.display import display
from pymongo import MongoClient
from config import mongoURI
import pandas as pd

client = MongoClient(mongoURI)
db_name = client['customers_analytics']
collection_name = db_name['customers_analytics']

docs = collection_name.find().limit(10)

df = pd.DataFrame(docs)

# print(df.head())

df['Age'] = 2021 - df['Year_Birth']
df = df.rename(columns={'MntWines': "Wines", 'MntFruits':'Fruits', 'MntMeatProducts':'Meat',
 'MntFishProducts':'Fish', 'MntSweetProducts':'Sweets', 'MntGoldProds':'Gold'})
df = df.loc[:, ['Age', 'Wines', 'Fruits', 'Meat', 'Fish', 'Sweets', 'Gold']]
# print(df)

display(df)
