from os import system as s

s('ls storage > jn.txt')
fh = open('jn.txt')
l=len(fh.readlines())
fh.close()
s('rm jn.txt')

s('mkdir src')

for i in range(l):
	fh = open('./src/j' + str(i + 1) + '.py', 'w')
	v = r'''import pandas as pd
import numpy as np

df=pd.read_csv('./storage/ch''' + str(i + 1) + r'''.dat', header=None)
v=max(df[0].to_numpy())

fh=open('result.txt', 'a')
fh.write(str(v) + '\n')
fh.close()'''
	fh.write(v)
	fh.close()
