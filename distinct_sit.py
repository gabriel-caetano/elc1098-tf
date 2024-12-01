import pandas as pd

df = pd.read_csv('ds/União/sit_turma.csv')
# situacoes = set(df['Situação'])
for i in df:
    print(i)