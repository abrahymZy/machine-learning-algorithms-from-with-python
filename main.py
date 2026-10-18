from evaluate_algorthim import evaluate_algorthim
from evaluation_matrics import accuracy_metric
from simple_algorthim import *
from print_confusion_matrix import print_confusion_matrix
from split_data import *
from preprocessing import *
from evaluation_matrics import *
from read_csv import load_csv

from math import sqrt
from random import randrange

dataset = load_csv('data/pima-indians-diabetes.csv')

minmax = dataset_minmax(dataset)
# print(minmax)
# normalize_dataset(dataset, minmax)
# print(dataset)
mean = column_means(dataset)
stdevs = column_stdevs(dataset, mean)

# standradize_dataset(dataset, mean, stdevs)
# print(dataset)


# print("---------------------------------")

train , test = train_test_split(dataset)
predicted = random_algorthim(train, test)
predicted_zero = zero_rule_algorthim(train, test)
predicted_zero_reg = zero_rule_algorthim_regression(train, test)

# print(train)
print(predicted)
print(predicted_zero)
print(predicted_zero_reg)

# print (train)
# print(test)

# print(cross_validation_split(dataset,folds=6))

# مصفوفتان لقيم فعلية ومتوقعة مداها من 0 إلى 50 (فئات: 0، 10، 20، 30، 40، 50)
actual = [
     0,  0,  50,  0,  0,  0,  0,  0,  0,  0,
    10, 10, 10, 20, 10, 10, 10, 10, 10, 30,
    20, 20, 20, 20, 20, 10, 20, 20, 20, 20,
    50, 30, 30, 30, 30, 30, 10, 30, 30, 30,
    40, 40, 40, 40, 40, 40, 10, 40, 40, 40,
    50, 50, 50, 20, 50, 50, 50, 50, 50, 40
]

predicted = [
     0,  0, 30,  0,  0, 10,  0,  0,  0,  0,
    10, 10, 10,  0, 10, 10, 20, 10, 10, 10,
    20, 20, 20, 20, 10, 20, 20, 30, 20, 20,
    30, 30, 20, 30, 30, 30, 30, 30, 40, 30,
    40, 40, 40, 30, 40, 40, 40, 50, 40, 40,
    50, 50, 50, 50, 40, 50, 50, 50, 50, 50
]

unique , matrix = confusion_matrix(actual, predicted)

print("---------------------------------")
# print(unique)
# print(matrix)
print_confusion_matrix(matrix, list(unique))
print("---------------------------------")
print(f"Accuracy metric = {accuracy_metric(actual, predicted)}")
print(f"MAE metric = {MAE_metric(actual, predicted)}")
print(f"RMSE metric = {RMSE_metric(actual, predicted)}")


