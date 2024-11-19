import pandas as pd
import xlrd
from glob import glob

# list of ds files
dir = "../ds/"
files = [x.split('/')[-1] for x in glob(dir + '*.xls*')]

# load all files in ds
ds = {}
for f in files:
    ds[f] = pd.read_excel(dir + f)

# test loaded files
for f in files:
    print(f)
    print(ds[f].head())

