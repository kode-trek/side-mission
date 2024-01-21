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

b0 = 6.626903339843835
b1 = -2.1567927472224064e-05

x = range(9564, 9604)
x = np.array(x)

hx = []
for i in x:	hx.append((b0) + (b1) * x)
hx = np.array(hx)

print 'X' + '\t' + 'H()' + '\t\t\t' + 'Y' + '\t' + 'HIT'
print '-------------------------------------------'

flg = ''
c = 0
for i in x:
	hx = int(b0 + (i * b1))
	print str(int(i)) + '\t' + '[' + str(hx - 4) + '...' + str(hx + 4) + ']    ' + str((b0 + (i * b1)))[:6] + '\t' + '?'
	c += 1
