from random import randrange
def random_algorthim(train, test):
    output_values = [row[-1] for row in train]
    unique = list(set(output_values))
    
    predicted = []

    for _ in test:
        index = randrange(len(unique))
        predicted.append(unique[index])
    
    return predicted

def zero_rule_algorthim(train, test):
    output_values = [row[-1] for row in train]
    prediction = max(set(output_values), key=output_values.count)
    predicted = [prediction for _ in test]
    
    return predicted



def zero_rule_algorthim_regression(train, test):
    output_values = [i[-1] for i in train]
    prediction = sum(output_values) / float(len(output_values))

    predicted = [prediction for _ in test]

    return predicted


def zero_rule_algorthim_classification(train, test):
    output_values = [i[-1] for i in train]
    prediction = max(set(output_values), key=output_values.count)
    predicted = [prediction for _ in test]

    return predicted
