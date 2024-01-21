from func import *
if argv[1] == '':
	print '[FAILED] invalid number of argument(s).'
	print 'cdup --help'
	exit()
if argv[1] == '--help':
	print '[PATTERN] cdup <path-to-DIR>'
	print '*clusters files within a (folder) into multiple groups of files with'
	print 'the same size.'
	exit()
# v1: path to directory
v1 = argv[1]
# adds </>
v1 += "/"
# checks whether <v1> is a directory or not
if not isdir(v1):
	print '[FAILED] directory not found.'
	print '[PATTERN] cdup <path-to-DIR>'
	exit()
# makes a list of file(s) and folder(s) within <v1>
v2 = listdir(v1)
v3 = []
for i in v2:	v3.append((v1 + i, stat(v1 + i).st_size))
# doesn't cluster folder(s)
v4 = []
for i in v3:
	if not isdir(i[0]):	v4.append(i)
# makes a set of size-list
v5 = []
for i in v4:	v5.append(i[1])
v5 = set(v5)
# makes cluster(s) named after size of file(s) within each
for i in v5:
	try:		mkdir(v1 + str(i))
	except:	pass
# drops items inside clusters
for i in v4:
	try:	move(i[0], v1 + str(i[1]))
	except:
		print '[FAILED] permission denied!'
		exit()
# eliminates clusters with only 1 item
for i in v5:
	if len(listdir(v1 + str(i))) == 1:
		for f in listdir(v1 + str(i)):
			move(v1 + str(i) + '/' + f, v1)
			rmtree(v1 + str(i))
print '[OK] done.'
