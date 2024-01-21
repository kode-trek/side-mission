import pandas as pd

v1 = pd.read_csv('original.csv')

print 'name of variables (columns):\t',
for i in v1.columns[1:]:
	print i,

print ''
print 'number of samples (rows):\t', len(v1.index)

print ''
print 'a bird\'s eye view of the table:'
print ''
print v1[['C', 'D', 'E', 'F', 'G', 'H']].head()
print '.'
print '.'
print '.'
print v1[['C', 'D', 'E', 'F', 'G', 'H']].tail()
