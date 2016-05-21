import csv
import numpy as np

csv_obj = csv.reader(open('train.csv'))
csv_obj.next()

data = []

for i in csv_obj:
    data.append(i)

print data[0::,4]

