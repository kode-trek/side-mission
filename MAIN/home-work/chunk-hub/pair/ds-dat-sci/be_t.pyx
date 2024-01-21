#http://docs.cython.org/en/latest/src/userguide/memoryviews.html
from cython.view cimport array as cvarray
import numpy as np
from func import *
from is_ds import is_ds
from is_big import is_big
from be_ds import be_ds
from phtm import phtm
def bet():
	# ds: data-set
	try:	ds = argv[1]
	except:
		print '[FAILED] no <.CSV> supplied!'
		print 'pattern: be-t <data-set.CSV>'
		exit()
	# checks for <ds> availability.
	is_ds(ds)
	# checks for big-dat.
	is_big(ds)
	# displays a bird's-eye view of data-set.
	# col: real-name column(s)
	# qcol: alias-name column(s)
	# ncol: number of column(s)
	# nrow: number of row(s)
	# df: data-set
	(col, qcol, ncol, nrow, df) = be_ds(ds)
	if (ncol > 4) and (nrow > 16):	phtm(df, col, ncol, nrow)
	return (col, qcol, ncol, nrow, df)
