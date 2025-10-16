# Criar uma nova coluna com o mês da venda.

import pandas as pd

df = pd.read_csv('./dados_vendas.csv')

df['Data'] = pd.to_datetime(df['Data'])
df['Mês da Venda'] = df['Data'].dt.month

print(df)