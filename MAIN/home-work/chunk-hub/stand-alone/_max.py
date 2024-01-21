import pandas as pd

df = pd.read_csv('result.txt', header=None)
v = max(df[0].to_numpy())

print 'max is:\t' + str(v)
