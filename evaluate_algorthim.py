from split_data import train_test_split
from evaluation_matrics import accuracy_metric

def evaluate_algorthim(dataset, algorthim,split_ratio=0.8, *arge):
    train, test = train_test_split(dataset, split_ratio)
  
    test_set = list()
    for row in test:
        row_copy = list(row)
        row_copy[-1] = None
        test_set.append(row_copy)

    predicted = algorthim(train, test_set,*arge)
    actual = [row[-1] for row in test]

    accuracy = accuracy_metric(actual, predicted)
    
    return accuracy


