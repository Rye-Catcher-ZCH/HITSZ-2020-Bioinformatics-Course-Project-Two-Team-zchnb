import csv
with open('tmp.csv', 'w') as morgan:
    writer = csv.writer(morgan)
    with open('test_compound.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            new_row = row[2].strip('\t')
            writer.writerow([new_row])
            



