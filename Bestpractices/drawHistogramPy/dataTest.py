import numpy as np
from matplotlib import pyplot as plt


data = np.loadtxt('/home/kunpengjiang/project/gpuEikonal/build/log', int)

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
print(numInt)
print(numOth)
print(maxnum)

fig, ax = plt.subplots(figsize=(10,7))
ax.hist(data, 10)
plt.show()
plt.savefig("pinNumFrequency")
