from sys import argv

fh = open('stk.csv')
v = fh.readlines()
fh.close()
v1 = []
for i in v:	v1.append(i[:-1])
v = v1

# cleansing uname
w = ''
for i in argv[1]:
	if i == ',' or i == '=':	w += '_'
	else:											w += i

# cleansing upass
w2 = ''
for i in argv[2]:
	if i == ',' or i == '=':	w2 += '_'
	else:											w2 += i

# chk user
for i in v:
	if (w == i.split(',')[0]) and (w2 == i.split(',')[1]):
		fh = open('stage.txt', 'w');	fh.write('False');	fh.close()
		break
	else:
		fh = open('stage.txt', 'w');	fh.write('True');	fh.close()
