import os
import pandas as pd

origin_path = 'ds/01_original'
dest_path = 'ds/02_sv'
for sub in os.listdir(origin_path):
    split = sub.split('.')

    if len(split) < 2:
        for sub2 in os.listdir(f'{origin_path}/{sub}'):
            [name, ext] = sub2.split('.')
            if ext == 'xls':
                pd.read_excel(f'{origin_path}/{sub}/{sub2}', engine='xlrd').to_csv(f'{dest_path}/{sub}/{name}.csv', index=False, sep=",")

            elif ext == 'xlsx':
                pd.read_excel(f'{origin_path}/{sub}/{sub2}', engine='openpyxl').to_csv(f'{dest_path}/{sub}/{name}.csv', index=False, sep=",")
    else:
        [name, ext] = sub.split('.')
        if ext == 'xls':
            pd.read_excel(f'{origin_path}/{sub}', engine='xlrd').to_csv(f'{dest_path}/{name}.csv', index=False, sep=",")

        elif ext == 'xlsx':
            pd.read_excel(f'{origin_path}/{sub}', engine='openpyxl').to_csv(f'{dest_path}/{name}.csv', index=False, sep=",")