clear

declare -a jList
. act1.sh & jList[0]=$!
. act2.sh & jList[1]=$!

echo 'table of actor(s):'
echo ''

ps -p ${jList[0]} -o cmd,%cpu,%mem
ps -p ${jList[1]} -o cmd,%cpu,%mem

ps -p ${jList[0]} -o cmd,%cpu,%mem >> jList2;
ps -p ${jList[1]} -o cmd,%cpu,%mem >> jList2;

v1=$(wc -l < "jList2")
while [ $v1 -gt 2 ]
do
	v1=$(wc -l < "jList2")
	sleep 1
	rm jList2
	clear

	echo 'table of actor(s):'
	echo ''

	ps -p ${jList[0]} -o cmd,%cpu,%mem
	ps -p ${jList[1]} -o cmd,%cpu,%mem

	ps -p ${jList[0]} -o cmd,%cpu,%mem >> jList2;
	ps -p ${jList[1]} -o cmd,%cpu,%mem >> jList2;
done

. act_max.sh

rm jList2
