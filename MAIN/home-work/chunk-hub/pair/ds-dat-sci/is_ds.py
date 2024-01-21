from func import *
# checks for <ds> availability.
def is_ds(arg1):
	if not exists(arg1):
		print '[FAILED] file not found!'
		print 'pattern: be-t <data-set.CSV>'
		exit()
	if isdir(arg1):
		print '[FAILED] not a <.CSV> file.'
		print 'pattern: be-t <data-set.CSV>'
		exit()
