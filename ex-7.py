# Mostrar todas as vendas feitas por um vendedor específico.

import pandas as pd

df = pd.read_csv('./dados_vendas.csv')

print(df[df['Vendedor']=='Ana'])