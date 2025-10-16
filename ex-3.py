# Contar o número de linhas e colunas.

import pandas as pd

df = pd.read_csv('./dados_vendas.csv')

print(f'rows: {df.shape[0]}')