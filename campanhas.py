from pymongo import MongoClient
from config import mongoURI
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

# Conexão com o MongoDB
client = MongoClient(mongoURI)
db_name = client['customers_analytics']
collection_name = db_name['customers_analytics']
docs = collection_name.find()  # .limit(10)
# -----------

# Dataframe de docs
df = pd.DataFrame(docs)

plt.style.use('ggplot')

# Sim e não por campanhas
campanha1NS = list(df.loc[:, ['AcceptedCmp1']].value_counts().values)
campanha2NS = list(df.loc[:, ['AcceptedCmp2']].value_counts().values)
campanha3NS = list(df.loc[:, ['AcceptedCmp3']].value_counts().values)
campanha4NS = list(df.loc[:, ['AcceptedCmp4']].value_counts().values)
campanha5NS = list(df.loc[:, ['AcceptedCmp5']].value_counts().values)
campanhas = {'Não': [campanha1NS[0], campanha2NS[0], campanha3NS[0], campanha4NS[0], campanha5NS[0]],
             "Sim": [campanha1NS[1], campanha2NS[1], campanha3NS[1], campanha4NS[1], campanha5NS[1]]}
index_campanhas = ['Campanha 1', 'Campanha 2',
                   'Campanha 3', 'Campanha 4', 'Campanha 5']
df_campanhasSN = pd.DataFrame(campanhas, index=index_campanhas)
# df_campanhasSN.plot.barh(stacked=True)
# ----

# Totais de sim por campanha
acceptedCmps = df.loc[:, ['AcceptedCmp1', 'AcceptedCmp2',
                          'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']]
acceptedCmp1Sum = df['AcceptedCmp1']
acceptedCmp2Sum = df['AcceptedCmp2']
acceptedCmp3Sum = df['AcceptedCmp3']
acceptedCmp4Sum = df['AcceptedCmp4']
acceptedCmp5Sum = df['AcceptedCmp5']
response = df['Response']

print(df[response == 1].loc[:, ['Marital_Status']].value_counts())
print(df['Marital_Status'].value_counts())

# Pizza com os totais de sim por campanha
labels = ['1ª Campanha', '2ª Campanha', '3ª Campanha',
          '4ª Campanha', '5ª Campanha', 'Última Campanha']
campanhas = [
    acceptedCmp1Sum.sum(),
    acceptedCmp2Sum.sum(),
    acceptedCmp3Sum.sum(),
    acceptedCmp4Sum.sum(),
    acceptedCmp5Sum.sum(),
    response.sum()
]

df_totais = pd.DataFrame(campanhas, index=labels)
totalrow = pd.DataFrame([df_totais.sum()], index=['Total'])
display(df_totais.append(totalrow).style.hide_columns())
# df_totais.plot.pie(y=0, explode=(0, 0, 0, 0, 0, 0.1), autopct='%1.1f%%', figsize=(
#     9, 9), shadow=True, counterclock=False, label='Aceitação \npor campanhas', startangle=160)

# Barra horizontal do estado civil e educação 
response_details = df[response == 1].loc[:, [
    'Marital_Status', 'Education']].value_counts()
response_details.plot.barh(title='Clientes que aceitaram na última oferta')
