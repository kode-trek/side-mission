from os import mkdir

fh = open('stage.txt')
v = fh.readlines()
fh.close()
v1 = []
for i in v:	v1.append(i[:-1])
v = v1

# cleansing uname
w = ''
for i in v[0]:
	if i == ',' or i == '=':	w += '_'
	else:											w += i
v[0] = w
# cleansing upass
w = ''
for i in v[1]:
	if i == ',' or i == '=':	w += '_'
	else:											w += i
v[1] = w

fh = open('stk.csv', 'a')
fh.write(v[0] + ',' + v[1] + ',' + v[2] + ',' + v[3] + '\n')
fh.close()
