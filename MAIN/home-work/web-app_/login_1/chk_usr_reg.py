from sys import argv

fh = open('stk.csv')
v = fh.readlines()
fh.close()
v1 = []
for i in v:	v1.append(i[:-1])
v = v1

# cleanding uname
w = ''
for i in argv[1]:
	if i == ',' or i == '=':	w += '_'
	else:											w += i

# chk whether uname exists
for i in v:
	if w == i.split(',')[0]:
		fh = open('stage.txt', 'w');	fh.write('False');	fh.close()
		break
	else:
		fh = open('stage.txt', 'w');	fh.write('True');	fh.close()
