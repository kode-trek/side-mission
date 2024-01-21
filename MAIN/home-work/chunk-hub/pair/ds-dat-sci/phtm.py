from func import *
# arg1: data-set
# arg2: real-name column(s)
# arg3: number of column(s)
# arg4: number of row(s)
def phtm(arg1, arg2, arg3, arg4):
	htm = '''<meta charset="UTF-8">
<style>
	table, th, td {
	border: 1px solid black;
	border-collapse: collapse;
	text-align: center;
	padding: 8px;
}
</style>

<body>
	<h1>bird's-eye view:</h1>
	<table style="width:100%; border: 1px solid black;">
		<tr>
			<th>''' + 'ROW#' + '''</th>
			<th>''' + arg2[0] + '''</th>
			<th>''' + arg2[1] + '''</th>
			<th>''' + '...' + '''</th>
			<th>''' + arg2[-2] + '''</th>
			<th>''' + arg2[-1] + '''</th>
		</tr>
		<tr>
			<td>''' + str(1) + '''</td>
			<td>''' + str(arg1['q1'][0]) + '''</td>
			<td>''' + str(arg1['q2'][0]) + '''</td>
			<td>''' + '...' + '''</td>
			<td>''' + str(arg1['q' + str(arg3 - 1)][0]) + '''</td>
			<td>''' + str(arg1['q' + str(arg3)][0]) + '''</td>
		</tr>
		<tr>
			<td>''' + str(2) + '''</td>
			<td>''' + str(arg1['q1'][1]) + '''</td>
			<td>''' + str(arg1['q2'][1]) + '''</td>
			<td>''' + '...' + '''</td>
			<td>''' + str(arg1['q' + str(arg3 - 1)][1]) + '''</td>
			<td>''' + str(arg1['q' + str(arg3)][1]) + '''</td>
		</tr>
		<tr>
			<td>''' + '...' + '''</td>
			<td>''' + '...' + '''</td>
			<td>''' + '...' + '''</td>
			<td>''' + '...' + '''</td>
			<td>''' + '...' + '''</td>
			<td>''' + '...' + '''</td>
		</tr>
		<tr>
			<td>''' + str(arg4 - 1) + '''</td>
			<td>''' + str(arg1['q1'][arg4 - 2]) + '''</td>
			<td>''' + str(arg1['q2'][arg4 - 2]) + '''</td>
			<td>''' + '...' + '''</td>
			<td>''' + str(arg1['q' + str(arg3 - 1)][arg4 - 2]) + '''</td>
			<td>''' + str(arg1['q' + str(arg3)][arg4 - 2]) + '''</td>
		</tr>
		<tr>
			<td>''' + str(arg4) + '''</td>
			<td>''' + str(arg1['q1'][arg4 - 1]) + '''</td>
			<td>''' + str(arg1['q2'][arg4 - 1]) + '''</td>
			<td>''' + '...' + '''</td>
			<td>''' + str(arg1['q' + str(arg3 - 1)][arg4 - 1]) + '''</td>
			<td>''' + str(arg1['q' + str(arg3)][arg4 - 1]) + '''</td>
		</tr>
	</table>
</body>
'''
	if exists('out.htm'):
		print '[FAILED] <out.htm> exists!'
		exit()
	fh = open('out.htm', 'w'); fh.write(htm); fh.close()
	print '<out.htm> created!'
	exit()
