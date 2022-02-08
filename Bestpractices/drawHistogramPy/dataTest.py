import numpy as np
from matplotlib import pyplot as plt


data = np.loadtxt('/home/kunpeng/data/projects/gpuEikonal/build/log', int)

print(len(data))
numInt = 0
numOth = 0
maxnum = 0
for item in data:
    if isinstance(item, int):
        numInt = numInt + 1
        maxnum = max(maxnum, item)
    else:
        numOth = numOth + 1
    if item > 200:
        item = 200
print(numInt)
print(numOth)
print(maxnum)

fig, ax = plt.subplots(figsize=(10,7))
ax.hist(data, 10)
plt.xlabel("bucket size")
plt.ylabel("number of buckets")
plt.savefig("with")
