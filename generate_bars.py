import numpy as np
import matplotlib.pyplot as plt
import json

with open('all_distances.json') as f:
	dist = json.loads(f.read())

x = sorted([float(key) for key in dist.iterkeys()])
y = np.array([dist[str(xh)] for xh in x])

for p in range(0,121):
	if float(p/100) not in x:
		print p/100

N = len(x)
width = 0.6
ind = np.arange(N)
#print ind
bar_spec = [0]*122
bar_spec[21] = y[21]/2
bar = plt.bar(ind, y/2, width, color = 'b')
bar_special = plt.bar(ind,bar_spec, width, color = 'r')
plt.xticks((ind[0],ind[21],ind[40],ind[60],ind[80],ind[100],ind[120]),(0,0.21,0.4,0.6,0.8,1,1.2))
#plt.xticks(ind + width, x, rotation = 'vertical')
#plt.xlabel(x)
#plt.xlim(ind.min(), ind.max()+width)
plt.show()
"""
#x = np.arange(4)
#y = np.array([4,7,6,5])
f = plt.figure()
ax = f.add_axes([0.1, 0.1, 0.8, 0.8])
ax.bar(ind, y, align='center')
#ax.set_xticks(x)
ax.set_xticklabels(x)
f.show()
"""