import numpy as np
import argparse

import torch
from torch import nn


class poolingData(nn.Module):

    """Docstring for poolingData. """

    def __init__(self, poolsize):
        """TODO: to be defined. """
        nn.Module.__init__(self)
        self.nw = nn.AvgPool3d(poolsize)

    def forward(self, x):
        ans = self.nw(x)
        return ans

def process(sourceFile, aimFile, depth, full_size):
    """TODO: Docstring for main.
    :returns: TODO

    """
    aim_size = [[40, 1, 500], [40, 50, 50], [40, 500,500], [20, 50, 500]]

    print("loading data")
    data = np.loadtxt(sourceFile, float)
    print("reshaping data")
    data = np.reshape(data, (1, 1, depth, full_size, full_size), 'C')

    #z, y, x

    print("transforming data")

    #aimFile = "test{}x{}x{}.dat"
    for size in aim_size:
        x_data = torch.from_numpy(data)
        print("for size {}x{}x{}".format(size[0], size[1], size[2]))
        poolsize = (depth//size[0], full_size//size[1], full_size//size[2])
        op = poolingData(poolsize)
        print("writing")
        tmp = op.forward(x_data)
#        tmp = tmp[:,:,:,0,:]
        tmp = tmp.numpy()
        print(aimFile.format(size[0], size[1], size[2]))
        tmp = np.reshape(tmp, (1,-1), 'C')
        np.savetxt(aimFile.format(size[0], size[1], size[2]), tmp, delimiter='\t')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--depth", help="x dim", type=int, default=40)
    parser.add_argument("-f", "--full_size", help="y dim size", type=str, default=1500)
    parser.add_argument("-s", "--sourceFile", help="sourceFile name", type=str, default="/home/kunpengjiang/data/EikonalSolver/3DSpeedMap40x1500x1500.dat")
    parser.add_argument("-a", "--aimFile", help="aimFile name", type=str, default="3DSpeedMap{}x{}x{}")

    args = parser.parse_args()
    process(args.sourceFile, args.aimFile, args.depth, args.full_size)
