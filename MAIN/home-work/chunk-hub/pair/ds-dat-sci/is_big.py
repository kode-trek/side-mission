from func import *
def is_big(arg1):
	# elicits size of dataset-file.
	# returns size in kiB.
	ds_size = stat(arg1).st_size / 1000.0
	# checks for available free RAM.
	meminfo = dict((i.split()[0].rstrip(':'), int(i.split()[1])) \
						for i in open('/proc/meminfo').readlines())
	mem_kib = meminfo['MemFree']
	# big-dat or not?
	if not ds_size < mem_kib:
		print '[BIG-DATA] not enough free memory available!'
		exit()
