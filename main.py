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
civil.plot.barh()

internet = df["NumWebPurchases"].sum()
catalago = df["NumCatalogPurchases"].sum()
loja = df["NumStorePurchases"].sum()

totais = pd.DataFrame({'Compras pela internet': [f'{internet:,}'.replace(',', '.')],
                       'Compras por catálago': [f'{catalago:,}'.replace(',', '.')],
                       'Compras em loja física': [f'{loja:,}'.replace(',', '.')],
})

display(totais.style.hide_index())