from numpy import product
from pandas.core.frame import DataFrame
from pymongo import MongoClient
from config import mongoURI
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt


client = MongoClient(mongoURI)
db_name = client['customers_analytics']
collection_name = db_name['customers_analytics']

docs = collection_name.find()

df = pd.DataFrame(docs)



#print(df.groupby("NumWebPurchases").mean())


#df1(df.loc[:, ["Marital_Status", 
#                "NumWebPurchases"]])
#compras = (df.loc[:, ["NumWebPurchases","MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts","MntGoldProds"]])

#print(df["NumWebPurchases"].sum())


#print(compras)
#print(compras.groupby(by=["NumWebPurchases", "compras" ]).sum().groupby(level=[0]).cumsum())

# firt = df[(df["NumWebPurchases"] <10)]["NumWebPurchases"]
# sec = df[(df["NumWebPurchases"] >=10) & (df["NumWebPurchases"] <20)]["NumWebPurchases"]
# thirt = df[(df["NumWebPurchases"] >=20)]["NumWebPurchases"]
# # print(firt, sec, thirt)

# print(df[(df["NumWebPurchases"] <10)]["Marital_Status"].value_counts())
# print(df[(df["NumWebPurchases"] >=10) & (df["NumWebPurchases"] <20)]["Marital_Status"].value_counts())
# print(df[(df["NumWebPurchases"] >=20)]["Marital_Status"].value_counts())

# print(df[(df["NumWebPurchases"] <10)]["Education"].value_counts())
# print(df[(df["NumWebPurchases"] >=10) & (df["NumWebPurchases"] <20)]["Education"].value_counts())
# print(df[(df["NumWebPurchases"] >=20)]["Education"].value_counts())
print(df["NumWebPurchases"].value_counts())

educacao = pd.DataFrame({'Até 5 compras': df[(df["NumWebPurchases"] <=5)]["Education"].value_counts(),
                         'Entre 05 e 10 compras': df[(df["NumWebPurchases"] >5) & (df["NumWebPurchases"] <10)]["Education"].value_counts(),
                         'Acima de 10 compras': df[(df["NumWebPurchases"] >=10)]["Education"].value_counts()                            
}).fillna(0).sort_values(by=['Até 5 compras'])


plt.style.use("ggplot")
educacao.plot.barh()



civil = pd.DataFrame({'Até 5 compras': df[(df["NumWebPurchases"] <=5)]["Marital_Status"].value_counts(),
                         'Entre 05 e 10 ': df[(df["NumWebPurchases"] >5) & (df["NumWebPurchases"] <10)]["Marital_Status"].value_counts(),
                         'Acima de 10': df[(df["NumWebPurchases"] >=10)]["Marital_Status"].value_counts()      
}).fillna(0)

plt.style.use("fivethirtyeight")
civil.plot.bar()

