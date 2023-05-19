import numpy as np
import argparse

def conv(val):
    try:
        return float(val)
    except ValueError:
        return val.decode('utf-8').split(":")[-1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dim", help="dim", type=int, default=1)
    parser.add_argument("-s", "--source_file", help="sourceFile name", type=str, default="/home/kp/data/data/LinearRegression/YearPredictionMSDSample")
    parser.add_argument("-t", "--train_file", help="train_file name", type=str, default="./trainTest")
    parser.add_argument("-r", "--response_file", help="response_file name", type=str, default="./responseTest")

    args = parser.parse_args()


    raw_data = np.loadtxt(args.source_file, converters=conv)

    np.savetxt(args.response_file, raw_data[:, 0: args.dim], delimiter=',', fmt='%.6f')
    np.savetxt(args.train_file, raw_data[:, args.dim: -1], delimiter=',', fmt='%.6f')
