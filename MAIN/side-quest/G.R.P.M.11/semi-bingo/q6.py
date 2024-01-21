import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from random import randint
from random import sample

def estimate_coef(x, y):
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x, m_y = np.mean(x), np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return(b_0, b_1)

v1 = pd.read_csv('original.csv')

x1 = np.array(v1['C'][:200])
y1 = np.array(v1['D'][:200])

# model
v = estimate_coef(x1, y1)
b_0 = v[0]
b_1 = v[1]

print 'b0:', b_0
print 'b1:', b_1
print 'H(X) = (b0) + (b1)X'
print ''

x2 = v1['C'][200:210]
y2 = v1['D'][200:210]
x2 = np.array(x2)
y2 = np.array(y2)

print 'X' + '\t' + 'H()' + '\t\t' + 'Y' + '\t' + 'HIT'
print '-------------------------------------------'

flg = ''
c = 0
for i in x2:
	h = int(b_0 + (i * b_1))
	if y2[c] in [h-1, h, h+1]:	flg = 'yes'
	else:						flg = 'no'
	print str(int(i)) + '\t' + '[' + str(h-1) + ', ' + str(h) + ', ' + str(h+1) + ']' + '\t' + str(y2[c]) + '\t' + flg
	c += 1
