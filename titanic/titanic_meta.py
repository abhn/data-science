import csv
import numpy as np

csv_obj = csv.reader(open('train.csv'))
csv_obj.next()

data = []

for i in csv_obj:
    data.append(i)

data = np.array(data)
survived = np.sum(data[0::,1].astype(np.float))
total = np.size(data[0::,1].astype(np.float))

women = data[0::, 4] == "female"
men = data[0::, 4] != "female"

women_on_board = data[women, 1].astype(np.float)
print np.sum(women_on_board) / np.size(women_on_board)

men_on_board = data[men, 1].astype(np.float) # % of men who survived
print np.sum(men_on_board) / np.size(men_on_board) # % of women who survived