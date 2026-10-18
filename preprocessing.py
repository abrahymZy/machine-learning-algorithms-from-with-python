from math import sqrt
def column_means(dataset):
    mean = [0 for i in range(len(dataset[0]))]

    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        mean[i] = sum(col_values) / float(len(dataset))
    
    return mean

def normalize_dataset(dataset, minmax):

    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])


def column_stdevs(dataset, mean):
    stdevs = [0 for i in range(len(dataset[0]))]

    for i in range(len(dataset[0])):
        power_values = [pow(row[i] - mean[i],2) for row in dataset]
        stdevs[i] = sum(power_values)
    
    stdevs = [sqrt(x/ float(len(dataset)-1)) for x in stdevs]
    return stdevs


def dataset_minmax(dataset):
    minmax = list()

    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax


def standradize_dataset(dataset, mean, stdevs):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - mean[i]) / stdevs[i]
