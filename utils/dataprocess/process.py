import numpy as np
import argparse

import torch
from torch import nn


class dopooling(nn.Module):

    """Docstring for poolingData. """

    def __init__(self, poolsize):
        """TODO: to be defined. """
        nn.Module.__init__(self)
        self.nw = nn.AvgPool3d(poolsize)

    def forward(self, x):
        ans = self.nw(x)
        return ans

def poolData(data, aim_size, aimFile, depth, full_size):
    """TODO: Docstring for main.
    :returns: TODO

    """

    print("reshaping data")
    data = np.reshape(data, (1, 1, depth, full_size, full_size), 'C')

    #z, y, x

    print("transforming data")

    aimFile = aimFile+"{}x{}x{}.dat"
    for size in aim_size:
        x_data = torch.from_numpy(data)
        print("for size {}x{}x{}".format(size[0], size[1], size[2]))
        poolsize = (depth//size[0], full_size//size[1], full_size//size[2])
        op = dopooling(poolsize)
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
    parser.add_argument("-a", "--aimFile", help="aimFile name", type=str, default="3DSpeedMap")

    args = parser.parse_args()


    aim_size = [[1, 1500, 1500]]
    print("aim_size")
    print(aim_size)
    print("loading data")
    data = np.loadtxt(args.sourceFile, float)
    poolData(data, aim_size, args.aimFile, args.depth, args.full_size)
