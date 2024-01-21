import pandas as pd

df = pd.read_csv('dat1.csv', header=None)
print max(df[:][1])
