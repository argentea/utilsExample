import numpy as np
import matplotlib.pyplot as mp
import argparse

from mpl_toolkits import mplot3d

def drawContour(data, aimFile,x_size=500, y_size=500, x_sizeT=300, y_sizeT=300):
    x = np.linspace(0, x_sizeT, x_sizeT)
    y = np.linspace(0, y_sizeT, y_sizeT)

    X,Y = np.meshgrid(x, y)
    data = np.reshape(data, (y_size, x_size), 'C')
    data = data[:x_sizeT, :y_sizeT]

    fig = mp.figure()
    mp.figure(figsize=(200,200))
    ax = mp.axes(projection='3d')
    ax.plot_surface(X, Y, data, cmap='viridis')

    print(aimFile.format(data.size//(y_size*x_size), y_size, x_size))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(aimFile.format(data.size//(y_size*x_size), y_size, x_size))
#    mp.show()
    mp.savefig(aimFile.format(data.size//(y_size*x_size), y_size, x_size))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--x_size", help="x dim", type=int, default=1500)
    parser.add_argument("-y", "--y_size", help="y dim size", type=int, default=1500)
    parser.add_argument("-tx", "--tx_size", help="ty dim size", type=int, default=1500)
    parser.add_argument("-ty", "--ty_size", help="ty dim size", type=int, default=1500)
    parser.add_argument("-s", "--sourceFile", help="sourceFile name", type=str, default="/home/kunpengjiang/project/gpuEikonal/build/fmmMeshlog")
    parser.add_argument("-a", "--aimFile", help="aimFile name", type=str, default="gpufsm{}x{}x{}")
    parser.add_argument("-g", "--graphType", help="graph type", type=str, default="drawContour")

    args = parser.parse_args()


    data = np.loadtxt(args.sourceFile, float)
    data = np.reshape(data, -1, 'C')
    drawContour(data, args.aimFile, args.x_size, args.y_size, args.tx_size, args.ty_size)
