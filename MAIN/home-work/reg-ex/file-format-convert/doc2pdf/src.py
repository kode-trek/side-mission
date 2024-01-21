import os

os.system('ls *.doc > LIST')

fh = file('LIST')
v1 = fh.readlines()
fh.close()

v2 = []
for i in v1:
	v2.append(i[:-1])

for i in v2:
	cmd = 'doc2pdf ' + i + ' &'
	os.system(cmd)
