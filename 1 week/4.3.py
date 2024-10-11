mport matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize = (16,9))
d1 = fig.add_subplot(121)
d2 = fig.add_subplot(122)

a = []
b = []
for i in set(df['Species']):
  a.append(list(df['Species']).count(i))
  b.append(i)
d1.pie(a, labels = b)
cnt1, cnt2, cnt3 = 0, 0, 0
for i in set(df['PetalLengthCm']):
    if i>1.2:
        cnt1 = cnt1 + 1
    if 1.5>i>1.2:
        cnt2 = cnt2 + 1
    if i>1.5:
        cnt3 = cnt3 + 1
d2.pie([cnt1, cnt2, cnt3], labels = ['>1,2', 'от 1,2 до 1,5', '>1,5'])
plt.show()