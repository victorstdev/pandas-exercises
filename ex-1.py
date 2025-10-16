# Carregar o CSV e exibir as 5 primeiras linhas.

import pandas as pd

df = pd.read_csv('dados_vendas.csv', nrows=5)

print(df)
