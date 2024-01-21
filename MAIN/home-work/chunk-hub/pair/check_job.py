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
