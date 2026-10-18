from math import sqrt
def accuracy_metric(actual, predicted):
    correct = 0

    for i in range(len(actual)):
        if (actual[i] == predicted[i]):
            correct+=1
    return correct / float(len(actual)) * 100.0

def confusion_matrix(actual, predicted):
    unique = set(actual)
    matrix = [list() for x in range(len(unique))]

    for i in range(len(unique)):
        matrix[i] = [0 for i in range(len(unique))]

    lockup = dict()

    for i, value in enumerate(unique):
        lockup[value] = i
    
    # fill matrix
    for i in range(len(actual)):
        x = lockup[actual[i]]
        y = lockup[predicted[i]]
        matrix[y][x] +=1
    
    return unique, matrix

def MAE_metric(actual, predicted):
    sum_between = 0

    for i in range(len(predicted)):
        sum_between += abs(predicted[i] - actual[i])

    return sum_between / float(len(actual))

def RMSE_metric(actual , predicted):
    sum_between = 0

    for i in range(len(predicted)):
        sum_between += pow(predicted[i] - actual[i], 2)
    
    return sqrt(sum_between / float(len(actual)))
