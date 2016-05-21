import csv
import numpy as np

test_file = open('test.csv')
csv_obj = csv.reader(test_file)
csv_obj.next()

data = []

for i in csv_obj:
    data.append(i)

data = np.array(data)

results = open('genderbased.csv', 'wb')
csv_res = csv.writer(results)

csv_res.writerow(['Survived', 'PassengerId'])

for row in data:
    if(row[3] == 'female'):
        csv_res.writerow([1, row[0]])

    else:
        csv_res.writerow([0, row[0]])

results.close()
test_file.close()