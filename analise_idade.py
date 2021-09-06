from IPython.core.display import display # Libs importadas
from pymongo import MongoClient
from config import mongoURI
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

plt.style.use('ggplot') # Estilo usado no graficos

client = MongoClient(mongoURI) # conexão com o MongoDB
db_name = client['customers_analytics']
collection_name = db_name['customers_analytics']

docs = collection_name.find() # consulta ao banco de dados

df = pd.DataFrame(docs) # Criação do Data Frame


# Limpeza dos dados: Preenchendo espaços vazios
df.isnull().sum().sort_values(ascending=False)
df.loc[(df['Income'].isnull() == True), 'Income'] = df['Income'].mean()

# Eliminação de linhas com ano de nacimento menor que 1921
for x in df.index:
    if df.loc[x, 'Year_Birth'] < 1921:
        df.drop(x, inplace=True)

df['Age'] = 2021 - df['Year_Birth'] # Adição de uma coluna "Age"

# Criação de coluna de Faixa Etária
cut_labels_Age = ['Young', 'Adult', 'Mature', 'Senior']
cut_bins = [0, 30, 45, 65, 82]
df['Faixas Etárias'] = pd.cut(df['Age'], bins=cut_bins, labels=cut_labels_Age)


# Renomeando as colunas de produtos
df = df.rename(columns={'MntWines': "Wines", 'MntFruits':'Fruits', 'MntMeatProducts':'Meat',
 'MntFishProducts':'Fish', 'MntSweetProducts':'Sweets', 'MntGoldProds':'Gold'})

df['Kids'] = df['Kidhome'] + df['Teenhome'] # Adição de uma coluna "Kids"

df["Has_Child"] = np.where(df['Kids'] > 0, "Has Child", "No Child") # Coluna que informa se o cliente tem criança ou adolecente

df['Expenses'] = df['Wines'] + df['Fruits'] + df['Meat'] + df['Fish'] + df['Sweets'] + df['Gold'] # coluna "Gastos"

df = df.drop(['Z_Revenue', 'Z_CostContact', 'Kidhome', 'Teenhome', '_id', 'Year_Birth', 'Dt_Customer', 'Recency', 'AcceptedCmp3', 
'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2', 'Complain', 'Response'], axis=1) 

display(df)


# Análise da relação entre idades e consumo----------------------------------------------------------------

age_df = df[['Faixas Etárias', 'Wines', 'Fruits', 'Meat', 'Fish', 'Sweets', 'Gold']] # criando Novo DF "age_df"

age_df = age_df.groupby('Faixas Etárias').mean() # Média dos gastos por Faixa Etária

display(age_df)

# Média dos gastos por Faixa Etária: Gráfico de barras
age_df[['Wines', 'Fruits', 'Meat', 'Fish', 'Sweets', 'Gold']].plot.bar(title= 'Média dos gastos por Faixa Etária')


# relação de filhos em casa com consumo------------------------------------------------------

kids_df = df[['Has_Child', 'Expenses']]

kids_df = kids_df.groupby('Has_Child').mean() # Média dos gastos de quem tem ou não criança

display(kids_df)

kids_df['Expenses'].plot.bar(title= 'Média dos gastos de quem tem ou não criança')



