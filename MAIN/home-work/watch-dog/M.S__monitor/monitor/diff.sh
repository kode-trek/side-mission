while :
do
	cat 'stk.dat'
	echo ''
	stat --printf="file-size:\t%s\n" stk.dat
	echo ''
	sleep 1
	clear
done
