import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, metrics

# load the <original.csv> dataset
v = pd.read_csv('original.csv')

# defining feature matrix(X) and response vector(y)
# 'D'
X = v[['C', 'D', 'E', 'G', 'H']]
X = np.array(X)
y = v['F']
y = np.array(y)

# splitting X and y into training and testing sets
X_train, X_test, y_train, y_test = \
train_test_split(X, y, test_size=0.4, random_state=1)

# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, y_train)

# regression coefficients
#print('Coefficients: \n', reg.coef_)

# variance score: 1 means perfect prediction
#print('Variance score: {}'.format(reg.score(X_test, y_test)))

vC = (X_test.transpose())[0]
vD = (X_test.transpose())[1]
vE = (X_test.transpose())[2]
vG = (X_test.transpose())[3]
vH = (X_test.transpose())[4]

#print 'C_TEST:', vC
#print 'D_TEST:', vD
#print 'E_TEST:', vE
#print 'G_TEST:', vG
#print 'H_TEST:', vH

#print ''

#print 'coef:', reg.coef_

pC = []
for i in vC:	pC.append(i * reg.coef_[0])
pC = np.array(pC)

pD = []
for i in vD:	pD.append(i * reg.coef_[1])
pD = np.array(pD)

pE = []
for i in vE:	pE.append(i * reg.coef_[2])
pE = np.array(pE)

pG = []
for i in vG:	pG.append(i * reg.coef_[3])
pG = np.array(pG)

pH = []
for i in vH:	pH.append(i * reg.coef_[4])
pH = np.array(pH)

py = pC + pD + pE + pG + pH

print 'score:', str(reg.score(X_test, y_test))[:4], '%'

sample_py = py[:40]
sample_y_test = y_test[:40]

print ''
print 'y^' + '\t' + 'int(y^)' + '\t\t' + 'y' + '\t' + 'HIT'
print '-----------------------------------'

flg = ''
for i in range(len(sample_py)):
	if	int(sample_y_test[i]) in (int(sample_py[i])-1 , int(sample_py[i]), int(sample_py[i])+1):
		flg = 'yes'
	else:
		flg = 'no'
	print	str(sample_py[i])[:5] + '\t' + \
			str((int(sample_py[i])-1 , int(sample_py[i]), int(sample_py[i])+1)) + '\t' + \
			str(int(sample_y_test[i])) + '\t' + flg
