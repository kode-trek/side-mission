import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, metrics

def score_it(X,y):
	## splitting X and y into training and testing sets
	X_train, X_test, y_train, y_test = \
	train_test_split(X, y, test_size=0.4, random_state=1)

	# create linear regression object
	reg = linear_model.LinearRegression()

	# train the model using the training sets
	reg.fit(X_train, y_train)

	# regression coefficients
	print('Coefficients: \n', reg.coef_)

	# variance score: 1 means perfect prediction
	print('Variance score: {}'.format(reg.score(X_test, y_test)))

# load the <original.csv> dataset
v = pd.read_csv('original.csv')

# defining feature matrix(X) and response vector(y)
# 'D'
X = v[['C', 'E', 'F', 'G', 'H']]
X = np.array(X)
y = v['D']
y = np.array(y)
#
score_it(X,y)
print ''

# 'E'
X = v[['C', 'D', 'F', 'G', 'H']]
X = np.array(X)
y = v['E']
y = np.array(y)
#
score_it(X,y)
print ''

# 'F'
X = v[['C', 'D', 'E', 'G', 'H']]
X = np.array(X)
y = v['F']
y = np.array(y)
#
score_it(X,y)
print ''

# 'G'
X = v[['C', 'D', 'E', 'F', 'H']]
X = np.array(X)
y = v['G']
y = np.array(y)
#
score_it(X,y)
print ''

# 'H'
X = v[['C', 'D', 'E', 'F', 'G']]
X = np.array(X)
y = v['H']
y = np.array(y)
#
score_it(X,y)
print ''
