from pymongo import MongoClient
from config import mongoURI
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

client = MongoClient(mongoURI)
db_name = client['customers_analytics']
collection_name = db_name['customers_analytics']

docs = collection_name.find() #.limit(10)

df = pd.DataFrame(docs)


# Totais por campanha
acceptedCmp1Sum = df.loc[:, ['AcceptedCmp1']].sum()
acceptedCmp2Sum = df.loc[:, ['AcceptedCmp2']].sum()
acceptedCmp3Sum = df.loc[:, ['AcceptedCmp3']].sum()
acceptedCmp4Sum = df.loc[:, ['AcceptedCmp4']].sum()
acceptedCmp5Sum = df.loc[:, ['AcceptedCmp5']].sum()
print()

meuplot = [acceptedCmp1Sum, acceptedCmp2Sum, acceptedCmp3Sum, acceptedCmp4Sum, acceptedCmp5Sum]
labels = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
# pd.DataFrame(meuplot).plot.pie(autopct='%1.1f%%', shadow=True, startangle=90, subplots=True)

print(pd.DataFrame(meuplot))
plt.show()