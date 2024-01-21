from sys import exit
from os import system as s

try:
	flag = 1
	while(flag):
		s('clear')
		print '1. pie'
		print '2. bar'
		print '3. scatter'
		print '4. line'
		print '5. 3D'
		print ''

		v = raw_input('chart: ')
		print ''

		if	v == '1':
			print 'pie chart!'
			flag = 0
		if	v == '2':
			print 'bar chart!'
			flag = 0
		if	v == '3':
			print 'scatter chart!'
			flag = 0
		if	v == '4':
			print 'line chart!'
			flag = 0
		if	v == '5':
			print '3D chart!'
			flag = 0
		else:
			pass
except:
	print ''
	exit()
