from pymongo import MongoClient
from config import mongoURI
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

plt.style.use('ggplot')


client = MongoClient(mongoURI)
db_name = client['customers_analytics']
collection_name = db_name['customers_analytics']

docs = collection_name.find()

df = pd.DataFrame(docs)

#  TABELA COM A QUANTIDADE DE CLIENTES POR ESCOLARIDADE
perc = df['Education'].value_counts()
display(pd.DataFrame(perc))

# BARRA COM QNTD DE CLIENTES POR ESCOLARIDADE
perc.plot.bar(edgecolor='black', figsize=(8,8))


# GANHO ANUAL / GASTO ANUAL POR FORMAÇÃO



#display(df.groupby('Education')['MntWines'].mean())
#gastos['gastos'] = gastos.sum(axis=1)




df = df.groupby('Education').mean().round(2) # SELEÇÃO POR ESCOLARIDADE
gastos = df[['MntWines',                     # AMOSTRA DAS COLUNAS DOS PRODUTOS
         'MntFruits', 
         'MntMeatProducts', 
         'MntFishProducts', 
         'MntSweetProducts', 
         'MntGoldProds']]

display(gastos)                             # TABELA
gastos.plot.barh(figsize=(12,12))           # GRÁFICO






gastoAnual = gastos.sum(axis=1)                           # TABELA GASTOS
ganhoAnual = df.groupby('Education')['Income'].mean()     # TABELA GANHOS

# UNIFICANDO AS TABELAS
gxg = {'Ganho Mensal': ganhoAnual.div(12).round(2), 'Gasto Mensal': gastoAnual} 
index_gxg = ['2n Cycle', 'Basic', 'Graduation', 'Master', 'PhD']                
gxg_df = pd.DataFrame(gxg, index=index_gxg)

display(gxg_df)                    # IMPRIMINDO TABELA                             
gxg_df.plot.barh(figsize=(10,10))  # IMPRIMINDO GRÁFICO









#display(df.groupby('Education')['Income'].mean())




