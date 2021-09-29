import csv
import numpy as np
from matplotlib import pyplot as plt

with open('./errlog', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    raw_data = list(reader);

print(len(raw_data))

data = list(map((lambda x: int(x[0])), raw_data))

numInt = 0
numOth = 0
for item in data:
    if isinstance(item, int):
        numInt = numInt + 1
    else:
        numOth = numOth + 1
print(numInt)
print(numOth)

fig, ax = plt.subplots(figsize=(10,7))
ax.hist(data, 50, (1, 50))
plt.show()
#plt.savefig("pinNumFrequency")
