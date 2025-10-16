# Filtrar vendas com quantidade maior que 5.

import pandas as pd

df = pd.read_csv('./dados_vendas.csv')

print(df[df['Quantidade'] > 5])