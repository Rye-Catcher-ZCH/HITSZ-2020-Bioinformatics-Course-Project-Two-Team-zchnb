#coding:utf-8
import matplotlib
#matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
import csv
from scipy import interpolate

plt.figure(1) # 创建图表1
plt.title('Precision/Recall Curve')# give plot a title
plt.xlabel('Recall')# make axis labels
plt.ylabel('Precision')
result = np.zeros([2,8000])
i = 0
with open('test_results.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        result[0][i] = row[0]
        result[1][i] = row[3]
        i = i+1

#y_true和y_scores分别是gt label和predict score
y_true = result[1]
y_scores = result[0]
precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
plt.figure(1)
#f = interpolate.interp1d(precision,recall,kind='cubic')
#x = np.linspace(0,1,8000)
#y = f(x)
plt.plot(precision, recall)
plt.show()
