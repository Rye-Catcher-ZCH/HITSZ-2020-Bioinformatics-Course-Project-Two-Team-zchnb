import csv

def add_tab(str):
    s = ''
    for i in str:
        s = s+i
        s = s+'\t' 
    return s

with open('tmp.csv', 'w') as morgan:
    writer = csv.writer(morgan)
    with open('validation_compound.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            new_row = add_tab(row[2])
            writer.writerow([new_row])
            



