# Verificar o tipo de dados de cada coluna.
import pandas as pd

df = pd.read_csv('./dados_vendas.csv')

print(df.info())