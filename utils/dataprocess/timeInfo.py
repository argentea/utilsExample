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

    algo_name = re.sub("time_breakdown*", "", file_name.split('/')[-1])
    return (algo_name, (file_name, time_interval))

def get_time_info(full_data, time_format):
    """Get avg and variance for each algo

    :full_data: {algo_name: [{metric_name: array[stages, time_interval}]]}
    :returns: {algo_name: [stages, avg, std]}

    """
    get_time = lambda x: x.total_seconds()
    if time_format == 'second':
        get_str = lambda x: str(get_time(x))
    elif time_format == 'date':
        get_str = lambda x: str(x)[:-3]
    else:
        print("time format not supported")
        exit(1)


    row_name = ["stage", "avg", "std"] 
    algo_info = {}
    for algo in full_data:
        algo_data = []
        for metrics in full_data[algo]:
            file_name, intervals = metrics
            stage_names = np.vectorize(str)(np.squeeze(np.array(intervals)[:, [0]], 1))
            intervals = np.squeeze(np.array(intervals)[:, [1]], 1)
            algo_data.append(intervals)
        algo_data = np.array(algo_data)

        algo_info[algo] = np.insert([stage_names, np.vectorize(get_str)(np.average(algo_data, 0)), np.vectorize(str)(np.std(np.vectorize(get_time)(algo_data), 0))], 0, row_name, 1)
        

    return algo_info



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time_format', choices=['date', 'second'], default='second')
    parser.add_argument('-f', '--file_name', type=str, nargs='+', help='file name of breakdown file')
    args = parser.parse_args()
    time_format = args.time_format

    full_data = {}
    for file_name in args.file_name:
        metrics = read_from_file(file_name)
        if metrics[0] in full_data:
            full_data[metrics[0]].append(metrics[1])
        else:
            full_data[metrics[0]] = [metrics[1]]
    infodata = get_time_info(full_data, time_format)
    for algo in infodata:
        np.savetxt(algo+"_info.csv", infodata[algo], delimiter=",", fmt="%s")

        table = tabulate(infodata[algo], tablefmt="fancy_grid")
        print(table)

