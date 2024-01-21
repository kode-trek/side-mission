from os import system as s

s('ssh vspades@192.168.1.106 ps -q `sed -n 1,1p tmp` -o state --no-headers > tmp2')
fh = open('tmp2');	v1.append(fh.readline()); fh.close()
#ssh vspades@192.168.1.106 ps -q `sed -n 2,2p tmp` -o state --no-headers
#ssh vspades@192.168.1.106 ps -q `sed -n 2,2p tmp` -o state --no-headers
