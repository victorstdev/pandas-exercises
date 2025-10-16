# Listar os produtos únicos vendidos.

import pandas as pd

df = pd.read_csv('./dados_vendas.csv')

print(df['Produto'].unique())