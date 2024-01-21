import matplotlib.pyplot as plt

#labale
v1 = []
#freq
v2 = []

fh = open('stk.dat')
v = fh.readlines()
fh.close()

v = v[:-1]
w = []
for i in v:	w.append(i[:-2])

for i in range(len(w)):
	if i%2 == 0:	v1.append(str(w[i].split('=')[1]))
	if i%2 != 0:	v2.append(int(w[i].split('=')[1]))

plt.bar(v1, v2)
plt.savefig('out.pdf')
