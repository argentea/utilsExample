import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as mp
import argparse
import os

def diffData(stddata, aimdata, outfileName, draw, printData):
    """TODO: Docstring for main.

    :arg1: TODO
    :returns: TODO

    """
    diffdata = []

    size = stddata.size

    diff = 0
    count = 0
    print(size)
    for i in range(size):
        if stddata[i] != 0:
            diff = max(diff, ((abs((stddata[i] - aimdata[i]))/stddata[i])))
            diffdata.append(abs((stddata[i] - aimdata[i]))/stddata[i])
            if abs(stddata[i] - aimdata[i])/stddata[i] > 0.2:
                count = count + 1
        else:
            diffdata.append(0)
    print("max different")
    print(diff)
    print(count)


    if draw != 0:
        fig, ax = plt.subplots(figsize=(10,7))
        ax.hist(diffdata, 20)
        plt.yscale('log', nonposy='clip')
        plt.show()
        #remove log in string
        plt.savefig(outfileName)
        print(outfileName+".png")
    if printData != 0:
#        diffdata.savetxt(outfileName+".csv", delimiter=" ")
        np.savetxt(outfileName+".csv", diffdata, delimiter=" ")
        print(outfileName+".csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--stdFileName", help="sourceFile name", type=str, default="/home/kunpengjiang/project/gpuEikonal/build/fmmlog")
    parser.add_argument("-a", "--aimFileName", help="aimFile name", type=str, default="/home/kunpengjiang/project/gpuEikonal/build/gpufsmlog")
    parser.add_argument("-g", "--drawgraph", help="draw diff distrubution graph", type=int, default=0)
    parser.add_argument("-p", "--printdata", help="print diff distrubution data", type=int, default=0)

    args = parser.parse_args()

    stddata = np.loadtxt(args.stdFileName, float)
    aimdata = np.loadtxt(args.aimFileName, float)
    stddata = np.reshape(stddata, -1, 'C')
    aimdata = np.reshape(aimdata, -1, 'C')

    filestd = os.path.basename(args.stdFileName)[:-3]
    fileaim = os.path.basename(args.aimFileName)[:-3]
    outfileName = filestd+"Vs"+fileaim

    diffData(stddata, aimdata, outfileName, args.drawgraph, args.printdata)
