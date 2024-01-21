import os

os.system('ls tmp/ > LST')

fh = file('LST')
v1 = fh.readlines()
fh.close()

v2 = []
for i in v1:
	v2.append(i[:-1])

l = len(v1)

c = 0
while(c < l):
	cmd = 'ffmpeg -i tmp/' + v2[c] + ' -strict experimental -c:a aac -async 1 ' + v2[c][:-4] + '.mp4 &'
	os.system(cmd)
	c += 1

flag = 1
while(flag):
	os.system('ps aux | grep "ffmpeg -i" > LOG')

	fh = open('LOG')
	v1 = fh.readlines()
	fh.close()

	if (len(v1) > 2):
		pass
	else:
		os.system('clear')
		print 'success',
		flag = 0
	os.system('sleep 1')
