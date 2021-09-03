from pymongo import MongoClient
from config import mongoURI
import pandas as pd


client = MongoClient(mongoURI)
db_name = client['customers_analytics']
collection_name = db_name['customers_analytics']

docs = collection_name.find().limit(10)

df = pd.DataFrame(docs)

print(df)