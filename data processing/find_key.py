import csv
with open('tmp2.csv', 'w') as tmp:
    writer = csv.writer(tmp)
    with open('test_dti.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row[1])
            writer.writerow([row[1]])

