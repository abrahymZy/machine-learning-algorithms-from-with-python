from math import sqrt
from random import randrange

dataset = [
    [50, 30],
    [20, 90],
    [30, 50],
    [10, 15],
    [11, 27],
    [25 , 17],

]

def dataset_minmax(dataset):
    minmax = list()

    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

def normalize_dataset(dataset, minmax):

    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])    
    

def column_means(dataset):
    mean = [0 for i in range(len(dataset[0]))]

    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        mean[i] = sum(col_values) / float(len(dataset))
    
    return mean


def column_stdevs(dataset, mean):
    stdevs = [0 for i in range(len(dataset[0]))]

    for i in range(len(dataset[0])):
        power_values = [pow(row[i] - mean[i],2) for row in dataset]
        stdevs[i] = sum(power_values)
    
    stdevs = [sqrt(x/ float(len(dataset)-1)) for x in stdevs]
    return stdevs

def standradize_dataset(dataset, mean, stdevs):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - mean[i]) / stdevs[i]

def train_test_split(dataset , split = 0.6):
    train = list()
    train_size = split * len(dataset)

    dataset_copy = list(dataset)

    while len(train) < train_size:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    
    return train , dataset_copy 


def cross_validation_split(dataset , folds=3):
    dataset_split = list()
    dataset_copy = list(dataset)

    fold_size = int(len(dataset) / folds)

    for i in range(folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))

        dataset_split.append(fold)

    return dataset_split


def accuracy_metric(actual, predicted):
    correct = 0

    for i in range(len(actual)):
        if (actual[i] == predicted[i]):
            correct+=1
    return correct / float(len(actual)) * 100.0

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



# مصفوفة الإرتباك
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
    
def print_confusion_matrix(matrix, labels):
    """
    طباعة مصفوفة الارتباك كجدول منسق بدون مكتبات خارجية.
    
    :param matrix: مصفوفة ثنائية الأبعاد (قائمة قوائم أو numpy array)
    :param labels: قائمة بأسماء التصنيفات (نصوص)
    """
    n = len(labels)
    str_matrix = [[str(cell) for cell in row] for row in matrix]

    # حساب أقصى عرض لكل عمود لضمان محاذاة دقيقة
    row_label_width = max(len(str(lbl)) for lbl in labels)
    
    col_widths = []
    for j in range(n):
        max_col = len(str(labels[j]))
        for i in range(n):
            max_col = max(max_col, len(str_matrix[i][j]))
        col_widths.append(max_col + 4)  # إضافة مسافة هامشية للقراءة

    total_table_width = row_label_width + sum(col_widths) + (n + 1)

    # 2. ترويسة الأعمدة (أسماء الفئات)
    header_row = f"{'':>{row_label_width}} |"
    for j, lbl in enumerate(labels):
        header_row += f"{str(lbl):^{col_widths[j]}}|"
    print(header_row)

    # خط فاصل متناسق تماماً مع عرض التسميات
    separator = "-" * (row_label_width + 1) + "+" + "+".join("-" * w for w in col_widths) + "+"
    print(separator)

    # 3. طباعة الصفوف (التصنيف الفعلي + القيم)
    for i in range(n):
        row_str = f"{str(labels[i]):>{row_label_width}} |"
        for j in range(n):
            row_str += f"{str_matrix[i][j]:^{col_widths[j]}}|"
        print(row_str)
        print(separator)



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

print(train)
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