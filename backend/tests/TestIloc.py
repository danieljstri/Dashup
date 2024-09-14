import pandas as pd

df = pd.read_csv('../app/fluxo.csv')

valor_receitas_marco = df.loc[df['RESULTADO'] == 'LUCROPREJUIZO', 'total'].values[0]

print(df.head())
print(valor_receitas_marco)
