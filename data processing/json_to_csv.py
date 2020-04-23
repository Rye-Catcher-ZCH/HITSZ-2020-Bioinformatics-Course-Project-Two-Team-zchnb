import json
import pandas as pd

f = open("1.json", 'r')
data = json.load(f)
#print(data)
with open('compound_smile.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in data.items()]