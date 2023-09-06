import csv

with open('hw.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    height_inches, weight_pounds = 0, 0
    count = 0
    for row in reader:
        count += 1
        height_inches += float(row[' "Height(Inches)"'])
        weight_pounds += float(row[' "Weight(Pounds)"'])
    print(
        f'Средний рост = {(height_inches / count) * 2.54} см\n'
        f'\bСредний вес = {(weight_pounds / count) * 0.45359237} кг')
