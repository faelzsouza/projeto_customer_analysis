from pymongo import MongoClient
from config import mongoURI
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

plt.style.use("ggplot")

client = MongoClient(mongoURI)
db_name = client['customers_analytics']
collection_name = db_name['customers_analytics']

docs = collection_name.find()

df = pd.DataFrame(docs)


# print(df.loc[:, ['Year_Birth', 'Marital_Status' ,'Income', 'MntWines']]) #Impressão das colunas desejadas 
# print(df.columns)


#Percentual de "Status Matrimonial"
perc = (df['Marital_Status'].value_counts())
display(perc)
perc.plot.pie(autopct="%1.1f%%", figsize=(9,9), label='')

#Idade dos entrevistados
for x in df.index:
    if df.loc[x, 'Year_Birth'] < 1921:
        df.drop(x, inplace=True)


df['Age'] = 2021 - df['Year_Birth']
age_df = df[['Age', 'Marital_Status', 'MntWines']]
print(age_df)

df['Age'].plot.hist(edgecolor='black', bins=20)

#Média de gastos com vinho e amount anual
gastos = df.mean()[['Income', 'Age']]
display(pd.DataFrame(gastos))










