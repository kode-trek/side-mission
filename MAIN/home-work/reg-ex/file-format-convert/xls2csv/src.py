#convert 1st sheet of <.xls> to <.csv>

import xlrd
import csv
import sys

with xlrd.open_workbook(sys.argv[1]) as wb:
	sh = wb.sheet_by_index(0)
	with open(sys.argv[2], 'wb') as f:
		c = csv.writer(f)
		for r in range(sh.nrows):
			c.writerow(sh.row_values(r))
