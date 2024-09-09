import pandas as pd

df = pd.read_csv('../app/fluxo.csv')

valor_receitas_marco = df.loc[df['RESULTADO'] == 'RECEITAS', 'marco'].values[0]

print(df.head())
print(valor_receitas_marco)
