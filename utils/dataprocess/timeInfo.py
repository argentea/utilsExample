import numpy as np
import argparse
import re
from datetime import datetime
from tabulate import tabulate



def read_from_file(file_name):
    """read a sigle file

    :file_name: file_name
    :returns: (algo_name, {stages: timeStamp}}

    """

    raw_data = np.loadtxt(file_name, dtype=str, delimiter=',', skiprows=1)
    time_metrics = np.apply_along_axis(lambda x:(x[0], datetime.strptime(x[1], '%Y-%m-%d %H:%M:%S.%f')), 1, raw_data)

    time_interval = []
    for i in range(len(time_metrics)):
        if i == 0:
            continue
        else:
            time_interval.append([time_metrics[i][0], time_metrics[i][1] - time_metrics[i-1][1]])
    time_interval.append(["Total", time_metrics[len(time_metrics)-1][1]-time_metrics[0][1]])

    algo_name = re.sub("_breakdown", "", file_name.split('/')[-1])
    return (algo_name, (file_name, time_interval))

    
def get_time_info(full_data):
    """Get avg and variance for each algo

    :full_data: {algo_name: [{metric_name: array[stages, time_interval}]]}
    :returns: {algo_name: [stages, avg, std]}

    """
    get_time = lambda x: x.total_seconds()
    algo_info = {}
    for algo in full_data:
        algo_data = []
        for metrics in full_data[algo]:
            file_name, intervals = metrics
            stage_names = np.squeeze(np.array(intervals)[:, [0]], 1)
            intervals = np.squeeze(np.array(intervals)[:, [1]], 1)
            algo_data.append(intervals)
        algo_data = np.array(algo_data)

        tmp = np.vectorize(get_time)(algo_data)
        algo_info[algo] = [stage_names , str(np.average(algo_data, 0)), np.std(np.vectorize(get_time)(algo_data), 0)]

    return algo_info



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', metavar='file', type=str, nargs='+', help='file name of breakdown file')
    args = parser.parse_args()

    full_data = {}
    for file_name in args.file_name:
        metrics = read_from_file(file_name)
        if metrics[0] in full_data:
            full_data[metrics[0]].append(metrics[1])
        else:
            full_data[metrics[0]] = [metrics[1]]
    infodata = get_time_info(full_data)
    print(infodata)

