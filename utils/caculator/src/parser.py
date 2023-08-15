import csv
import json


def algoParser(filename):
    """TODO: Docstring for algoParser.

    """
    field = []
    data = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        lineNo = 0
        for row in spamreader:
            if lineNo == 0:
                field = row
            else:
                data.append(row)
            lineNo = lineNo + 1
    print(field)
    print(data)

    return field, data

def devParser(filename):
    with open(filename) as jsonfile:
        data = json.load(jsonfile)

def dumpJson():
    jsondata = {}
    caculation = {}
    bandwith = {}

    caculation['single_precision'] = 16384
    caculation['double_precision'] = 16384
    print(json.dump(jsondata))


if __name__ == "__main__":
    algoParser("../algo/kmeans.csv")
