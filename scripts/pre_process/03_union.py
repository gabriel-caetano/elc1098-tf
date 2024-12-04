import os
import pandas as pd

origin_path = 'ds/03_manual'
dest_path = 'ds/04_union'

dfs = []
for sub in os.listdir(origin_path):
    split = sub.split('.')

    if len(split) == 2:
        [name, ext] = split
        dfs.append(pd.read_csv(f'{origin_path}/{sub}', sep=","))

pd.concat(dfs).to_csv(f'{dest_path}/sit_turma.csv', index=False, sep=",")

dfs = []
for sub in os.listdir(origin_path+'/Ingressantes e Formandos'):
    split = sub.split('.')

    if len(split) == 2:
        [name, ext] = split
        src = pd.read_csv(f'{origin_path}/Ingressantes e Formandos/{sub}', sep=",")
        centro = sub.split(' ')[0]
        src['CENTRO'] = centro
        dfs.append(src)

pd.concat(dfs).to_csv(f'{dest_path}/ingr_form.csv', index=False, sep=",")
