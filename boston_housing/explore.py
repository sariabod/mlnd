import pandas as pd

d = pd.read_csv('housing.csv')


print(d[d['RM']>7.99])
print(d[d['RM']>7.99].mean())

print(d[(d['LSTAT']>32) & (d['RM']<5)])
print(d[(d['LSTAT']>32) & (d['RM']<5)].mean())

print(d[(d['LSTAT']<20) & (d['LSTAT']>17) & (d['RM']>5) & (d['RM']<6)])
print(d[(d['LSTAT']<20) & (d['LSTAT']>17) & (d['RM']>5) & (d['RM']<6)].mean())
