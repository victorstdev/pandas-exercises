# Calcular o total de vendas (soma da coluna Total).

import pandas as pd

df = pd.read_csv('./dados_vendas.csv')

print(f'Total de vendas: R${df['Total'].sum()}')