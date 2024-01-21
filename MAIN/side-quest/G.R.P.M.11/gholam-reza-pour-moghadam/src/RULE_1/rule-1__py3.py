import pandas as pd
import numpy as np

df = pd.read_csv('T.csv')

v1 = np.array(df['A'][1:])
v2 = np.array(df['C12'])
v3 = np.array(df['B'])

try:    c = int(input('ID: '))
except:	c = 9466

i = np.array(df[df['C'] == c]['B'])[0]

b1 = int((c - 80) / np.array(df['C12'][i - 1]))
b2 = int((c - 80) / np.array(df['C24'][i - 1]))
b3 = int((c - 80) / np.array(df['C33'][i - 1]))
b4 = int((c - 80) / np.array(df['C35'][i - 1]))
b5 = int((c - 80) / np.array(df['C39'][i - 1]))

k = 0
for j in [b1,b2,b3,b4,b5]:
	w = []
	if j in v3:
		w.append(int(np.array(df['D'][j-2])))
		w.append(int(np.array(df['D'][j-1])))
		w.append(int(np.array(df['D'][j])))

		w.append(int(np.array(df['E'][j-2])))
		w.append(int(np.array(df['E'][j-1])))
		w.append(int(np.array(df['E'][j])))

		w.append(int(np.array(df['F'][j-2])))
		w.append(int(np.array(df['F'][j-1])))
		w.append(int(np.array(df['F'][j])))

		w.append(int(np.array(df['G'][j-2])))
		w.append(int(np.array(df['G'][j-1])))
		w.append(int(np.array(df['G'][j])))

		w.append(int(np.array(df['H'][j-2])))
		w.append(int(np.array(df['H'][j-1])))
		w.append(int(np.array(df['H'][j])))

		flg = []
		if (np.array(df['D'][i])) in w:	flg.append('yes')
		else:																flg.append('no')
		if (np.array(df['E'][i])) in w:	flg.append('yes')
		else:																flg.append('no')
		if (np.array(df['F'][i])) in w:	flg.append('yes')
		else:																flg.append('no')
		if (np.array(df['G'][i])) in w:	flg.append('yes')
		else:																flg.append('no')
		if (np.array(df['H'][i])) in w:	flg.append('yes')
		else:																flg.append('no')

		if (k == 0):	print ('D:', w, '\t', int(np.array(df['D'][i])), '\t', flg[0])
		if (k == 1):	print ('E:', w, '\t', int(np.array(df['E'][i])), '\t', flg[1])
		if (k == 2):	print ('F:', w, '\t', int(np.array(df['F'][i])), '\t', flg[2])
		if (k == 3):	print ('G:', w, '\t', int(np.array(df['G'][i])), '\t', flg[3])
		if (k == 4):	print ('H:', w, '\t', int(np.array(df['H'][i])), '\t', flg[4])

	k += 1

input('press ENTER to EXIT...')
