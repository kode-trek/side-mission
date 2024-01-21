import pandas as pd
import numpy as np
from math import modf

df = pd.read_csv('T.csv')

try:	a = input('A: '); a = int(a)
except:	a = 0

c12 = np.array(df['C12'])
c24 = np.array(df['C24'])
c33 = np.array(df['C33'])
c35 = np.array(df['C35'])
c39 = np.array(df['C39'])

v1 = a / c12
v2 = a / c24
v3 = a / c33
v4 = a / c35
v5 = a / c39

w = []
for i in v1:
        w.append(int(i))
v1 = np.array(w)

w = []
for i in v2:
        w.append(int(i))
v2 = np.array(w)

w = []
for i in v3:
        w.append(int(i))
v3 = np.array(w)

w = []
for i in v4:
        w.append(int(i))
v4 = np.array(w)

w = []
for i in v5:
        w.append(int(i))
v5 = np.array(w)

w = []
for i in v1:
	if i in np.array(df['B']):
		w.append(int(np.array(df['D'][i-1])))
		w.append(int(np.array(df['E'][i-1])))
		w.append(int(np.array(df['F'][i-1])))
		w.append(int(np.array(df['G'][i-1])))
		w.append(int(np.array(df['H'][i-1])))

k = pd.Index(w)
k = k.value_counts()
k.to_csv('q1.csv', header=False)

w = []
for i in v2:
	if i in np.array(df['B']):
		w.append(int(np.array(df['D'][i])))
		w.append(int(np.array(df['E'][i])))
		w.append(int(np.array(df['F'][i])))
		w.append(int(np.array(df['G'][i])))
		w.append(int(np.array(df['H'][i])))

k = pd.Index(w)
k = k.value_counts()
k.to_csv('q2.csv', header=False)

w = []
for i in v3:
	if i in np.array(df['B']):
		w.append(int(np.array(df['D'][i])))
		w.append(int(np.array(df['E'][i])))
		w.append(int(np.array(df['F'][i])))
		w.append(int(np.array(df['G'][i])))
		w.append(int(np.array(df['H'][i])))

k = pd.Index(w)
k = k.value_counts()
k.to_csv('q3.csv', header=False)

w = []
for i in v4:
	if i in np.array(df['B']):
		w.append(int(np.array(df['D'][i])))
		w.append(int(np.array(df['E'][i])))
		w.append(int(np.array(df['F'][i])))
		w.append(int(np.array(df['G'][i])))
		w.append(int(np.array(df['H'][i])))

k = pd.Index(w)
k = k.value_counts()
k.to_csv('q4.csv', header=False)

w = []
for i in v5:
	if i in np.array(df['B']):
		w.append(int(np.array(df['D'][i])))
		w.append(int(np.array(df['E'][i])))
		w.append(int(np.array(df['F'][i])))
		w.append(int(np.array(df['G'][i])))
		w.append(int(np.array(df['H'][i])))

k = pd.Index(w)
k = k.value_counts()
k.to_csv('q5.csv', header=False)
