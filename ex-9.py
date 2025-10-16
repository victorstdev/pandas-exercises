# Verificar quantas vendas foram feitas em São Paulo.

import pandas as pd

df = pd.read_csv('./dados_vendas.csv')

print(f'Quantidade de vendas feitas em São Paulo: {df[df['Cidade']=='São Paulo'].shape[0]}')