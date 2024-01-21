import pandas as pd
import numpy as np

df = pd.read_csv('T.csv')

v1 = np.array(df['A'][1:])
v2 = np.array(df['C12'])
v3 = np.array(df['B'])

try:		c = input('ID: ')
except:	c = 9466

i = np.array(df[df['C'] == c]['B'])

b1 = (c - 80) / np.array(df['C12'][i - 1])
b2 = (c - 80) / np.array(df['C24'][i - 1])
b3 = (c - 80) / np.array(df['C33'][i - 1])
b4 = (c - 80) / np.array(df['C35'][i - 1])
b5 = (c - 80) / np.array(df['C39'][i - 1])

k = 0
for j in [b1,b2,b3,b4,b5]:
	w = []
	if j in v3:
		w.append(np.array(df['D'][j-2])[0])
		w.append(np.array(df['D'][j-1])[0])
		w.append(np.array(df['D'][j])[0])

		w.append(np.array(df['E'][j-2])[0])
		w.append(np.array(df['E'][j-1])[0])
		w.append(np.array(df['E'][j])[0])

		w.append(np.array(df['F'][j-2])[0])
		w.append(np.array(df['F'][j-1])[0])
		w.append(np.array(df['F'][j])[0])

		w.append(np.array(df['G'][j-2])[0])
		w.append(np.array(df['G'][j-1])[0])
		w.append(np.array(df['G'][j])[0])

		w.append(np.array(df['H'][j-2])[0])
		w.append(np.array(df['H'][j-1])[0])
		w.append(np.array(df['H'][j])[0])
#		w = [25,9,3,32,13,7,36,26,8,37,31,31,38,34,33]
		flg = []
		if (np.array(df['D'][i])[0]) in w:	flg.append('yes')
		else:																flg.append('no')
		if (np.array(df['E'][i])[0]) in w:	flg.append('yes')
		else:																flg.append('no')
		if (np.array(df['F'][i])[0]) in w:	flg.append('yes')
		else:																flg.append('no')
		if (np.array(df['G'][i])[0]) in w:	flg.append('yes')
		else:																flg.append('no')
		if (np.array(df['H'][i])[0]) in w:	flg.append('yes')
		else:																flg.append('no')
#		flg = [no, no, no, yes, no]
		if (k == 0):	print 'D:', w, '\t', np.array(df['D'][i])[0], '\t', flg[0]
		if (k == 1):	print 'E:', w, '\t', np.array(df['E'][i])[0], '\t', flg[1]
		if (k == 2):	print 'F:', w, '\t', np.array(df['F'][i])[0], '\t', flg[2]
		if (k == 3):	print 'G:', w, '\t', np.array(df['G'][i])[0], '\t', flg[3]
		if (k == 4):	print 'H:', w, '\t', np.array(df['H'][i])[0], '\t', flg[4]

	k += 1
