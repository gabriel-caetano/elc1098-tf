import pandas as pd

df = pd.read_csv('ds/União/sit_turma.csv')
print(len(df))
profs = list(set(df["Professor"]))
print(profs)
print(df.head())
sub = df[df["Professor"] == profs[0]]

print(sub.head())
print(len(sub))

sub = df[df["Professor"] == profs[1]]

print(sub.head())
print(len(sub))

sub = df[df["Professor"] == profs[2]]

print(sub.head())
print(len(sub))