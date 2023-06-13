import numpy as np
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', metavar='file', type=str, nargs='+', help='file name of breakdown file')
    args = parser.parse_args()
