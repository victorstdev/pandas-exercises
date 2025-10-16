# Ordenar os dados pelo valor total da venda (decrescente).

import pandas as pd

df = pd.read_csv('./dados_vendas.csv')

print(df.sort_values('Total', ascending=False))