from scipy.interpolate import RegularGridInterpolator
import numpy as np
import matplotlib.pyplot as mp
import argparse


def gridInterpolator(data, x, y, z, tx, ty, tz, aimFile):
    """TODO: Docstring for gridInterpolator.

    """
    data = np.reshape(data, (z, y, x), 'C')
    print(data.shape)
    gx = np.linspace(0, x, x, endpoint=False)
    gy = np.linspace(0, y, y, endpoint=False)
    gz = np.linspace(0, z, z, endpoint=False)
    interpolator_function = RegularGridInterpolator((gz,gy,gx), data)

    finalgrid = []
    for iz in range(tz+1):
        for iy in range(ty+1):
            for ix in range(tx+1):
                finalgrid.append([iz/tz*(z-1), iy/ty*(y-1), ix/tx*(x-1)])

    finalData = interpolator_function(finalgrid)
    finalData = np.array(finalData)
    print(aimFile.format(tz,ty,tx))
    np.savetxt(aimFile.format(tz,ty,tx), finalData, delimiter='\t')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--x_size", help="x dim size", type=int, default=500)
    parser.add_argument("-y", "--y_size", help="y dim size", type=int, default=50)
    parser.add_argument("-z", "--z_size", help="z dim size", type=int, default=20)
    parser.add_argument("-tx", "--tx_size", help="x dim size of result", type=int, default=20)
    parser.add_argument("-ty", "--ty_size", help="y dim size of result", type=int, default=20)
    parser.add_argument("-tz", "--tz_size", help="z dim size of result", type=int, default=40)
    parser.add_argument("-s", "--sourceFile", help="sourceFile name", type=str, default="/home/kunpengjiang/data/EikonalSolver/tmp20x50x500")
    parser.add_argument("-a", "--aimFile", help="aimFile name", type=str, default="interData{}x{}x{}")

    args = parser.parse_args()


    data = np.loadtxt(args.sourceFile, float)
    data = np.reshape(data, -1, 'C')
    gridInterpolator(data, args.x_size, args.y_size, args.z_size, args.tx_size, args.ty_size, args.tz_size, args.aimFile)
