from utils.Drawgraph import drawjet
from utils.diffData import diffData
from utils.process import poolData
import numpy as np

data = np.loadtxt("/home/kunpengjiang/project/gpuEikonal/build/gpufsmlog", float)
data = np.reshape(data, -1, 'C')
drawjet(data, "nothing")
