import pandas as pd
import numpy as np

df=pd.read_csv('./storage/ch2.dat', header=None)
v=max(df[0].to_numpy())

fh=open('result.txt', 'a')
fh.write(str(v) + '\n')
fh.close()