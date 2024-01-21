from sys import argv
from os import walk
from itertools import permutations

# returns reversed list. (ex. [b,a] for [a,b])
def rev(arg1):
 v1 = arg1
 v2 = []
 for i in reversed(v1): v2.append(i)
 return v2

# v1: directory-name
v1 = argv[1]
# v2: file-name(s) in [v1]
v2 = next(walk(v1), (None, None, []))[2]
# v3: paire(s)
v3 = []
for i in v2:
 for j in v2:
  v3.append([i,j])
v3 = [i for i in v3 if i[0] != i[1]]
# v4: eliminates duplicated-pairs (ex. [a,b] & [b,a]) in [v3]
v4 = []
for i in v3:
 if rev(i) not in v4: v4.append(i)
for i in v4: print(i)
