import csv
tmp = open('test_protein.csv', 'w')
tmp2 = open('tmp2.csv', 'r')
tmp3 = open('protein.csv', 'r')
writer = csv.writer(tmp)
reader_1 = csv.reader(tmp2)
reader_2 = csv.reader(tmp3)
reader_2 = list(reader_2)
for row_i in reader_1:
    for row_j in reader_2:
        if row_i[0] == row_j[0]:
            writer.writerow(row_j)
            break 


