import pandas as pd

c=0
while(True):
	try:
		df = pd.read_csv('stk.csv', header=None, nrows=1000000, skiprows = range(0,c))
		print max(df[:][0])
		c += 1000000
	except:
		break
