import numpy as np
import matplotlib.pyplot as mp
import argparse

def drawGraph(data, aimFile,x_size=500, upperbound=10, y_size=1):
    """TODO: Docstring for main.
    """

    depth = data.size//x_size;
    data = np.reshape(data, (depth, x_size), 'C')

    data = data+1
    data = np.log(data)
    for i in range(depth):
        for j in range(x_size):
            if data[i][j] > upperbound:
                data[i][j] = upperbound 



    '''log version
    for i in range(depth):
        for j in range(x_size):
            if np.log(data[i][j]) > upperbound:
                data[i][j] = np.exp(upperbound)
    '''


    aimFileName = aimFile+"{}x{}x{}"
    mp.figure(aimFile.format(depth//y_size, y_size, x_size), figsize=(x_size/10, depth/10),facecolor='lightgray')
    mp.title(aimFile.format(depth//y_size, y_size, x_size))
    mp.grid(linestyle=":")
    mp.imshow(data, cmap='jet')
    mp.colorbar()
    mp.savefig(aimFile.format(depth//y_size, y_size, x_size))
    print(aimFile.format(depth//y_size, y_size, x_size))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--x_size", help="x dim", type=int, default=500)
    parser.add_argument("-y", "--y_size", help="y dim size", type=int, default=1)
    parser.add_argument("-u", "--upperbound", help="log upperbound", type=int, default=10)
    parser.add_argument("-s", "--sourceFile", help="sourceFile name", type=str, default="/home/kunpengjiang/project/gpuEikonal/build/gpufsmlog")
    parser.add_argument("-a", "--aimFile", help="aimFile name", type=str, default="./gpufsm")

    args = parser.parse_args()


    data = np.loadtxt(args.sourceFile, float)
    data = np.reshape(data, -1, 'C')
    drawGraph(data, args.aimFile, args.x_size, args.upperbound, args.y_size)
