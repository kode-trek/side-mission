from func import *
def be_ds(arg1):
	# puts the entire data-set on memory
	try:	df = pd.read_csv(arg1)
	except:
		print '[FAILED] not a <.CSV> file.'
		print 'pattern: be-t <data-set.CSV>'
		exit()
	# col[]: keeps hold of real name(s) of column(s)
	col = []
	for i in df.columns:	col.append(i)
	# ncol: keeps number of column(s)
	ncol = len(df.columns)
	# assigns alias name(s), starting from <q1> up to <qn>.
	# thus, calling column(s) later with their new name(s).
	c = 1
	qcol = []
	for i in range(ncol):
		qcol.append('q' + str(c))
		c += 1
	df.columns = qcol
	# nrow: keeps number of row(s)
	nrow = len(df.index)
	# views
	# number of col|row
	print 'number of column(s):\t', ncol
	print 'number of row(s):\t', nrow
	print ''
	# column(s)
	print 'column(s)'
	print '---------'
	if ncol <= 4:
		for i in range(ncol):	print qcol[i] + ': ' + str(col[i])
	else:
		print qcol[0] + ': ' + str(col[0])
		print qcol[1] + ': ' + str(col[1])
		print '...'
		print qcol[ncol - 2] + ': ' + str(col[ncol - 2])
		print qcol[ncol - 1] + ': ' + str(col[ncol - 1])
	print ''
	# returns
	return (col, qcol, ncol, nrow, df)
