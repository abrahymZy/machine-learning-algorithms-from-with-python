from csv import reader

def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)

    for i in range(len(dataset[0])):
        str_to_column_number(dataset, i)
        
    return dataset


def str_to_column_number(dataset, column_index):
    for row in dataset:
        if str(row[column_index]).find('.') > -1:
            row[column_index] = float(row[column_index])
        else:
            row[column_index] = int(row[column_index])


