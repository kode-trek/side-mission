import pandas as pd

v = pd.read_csv('1.csv', header=None, low_memory=False)

w = v[[2,3,4,5,6,7]][:9484]
w.columns = ['C', 'D', 'E', 'F', 'G', 'H']
print w.head()
w.to_csv('q.csv')
