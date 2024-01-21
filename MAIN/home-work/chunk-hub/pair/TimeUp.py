import thread
import time

def hi():
	v = raw_input('name: ')
	print v
	thread.interrupt_main()

def tu(arg1):
	for i in range(arg1):	time.sleep(arg1)
	try:
		if v[0]:	pass
	except:
		print 'Time Up!'
		thread.interrupt_main()

try:
	thread.start_new_thread(tu, (2,))
	thread.start_new_thread(hi, ())
except:
	pass

try:
	while True:	pass
except:
	print 'END'
