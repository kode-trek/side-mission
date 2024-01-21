import os

def isEmpty(arg1):
	fh = open(arg1)
	v1 = fh.readline()
	fh.close()
	if(v1 == ''):
		return True


def chunkIt(arg1):
	flg = 1
	os.system('mkdir ./storage')
	c = 0
	n = 1
	while(flg == 1):
		nam = './storage/ch' + str(n) + '.dat'
		cmd = 'awk "NR >= ' + str(c + 1) + ' && NR <= ' + str(c + 2000000) + '" ' + arg1 + ' > ' + nam
		print nam
		os.system(cmd)
		c += 2000000
		n += 1
		if isEmpty(nam):
			flg = 0
			os.system('rm ' + nam)

chunkIt('stk.csv')

#awk 'NR >= 1 && NR <= 2' stk.csv > ch1.dat &
#awk 'NR >= 3 && NR <= 4' stk.dat > ch2.dat &
