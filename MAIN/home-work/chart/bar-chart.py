import numpy as np
import pandas as pd

v1 = np.random.randint(-8, 8, size=16)

df1 = pd.DataFrame(v1)
c = df1[0].value_counts()
v2 = []
for i in v1:
	v2.append(c[i])

f = (c/max(c)*100).round()
v3 = []
for i in v1:
	v3.append(f[i])

print pd.DataFrame({
										'number':			v1,
										'count':			v2,
										'percentage':	v3,
										})
