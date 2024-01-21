from os import system as s
from sys import argv

try:
	s('sudo apt-get install -y xchm')
	s('xchm ' + argv[1] + ' & 2> /dev/null')
except:
	pass
