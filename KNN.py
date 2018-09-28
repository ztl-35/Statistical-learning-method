import numpy as np
import matplotlib.pyplot as plt
import math
x = np.array([[3, 0.5],
              [2, 0.5],
              [3, 0.5],
              [3, 4.7],
              [4, 4],
              [5, 4.5],
              [6, 3.1],
              [5, 4],
              [4, -0.1],
              [4, -1]])
y = np.array([-1, -1, -1, 1, 1, 1, 1, 1, -1, -1])

plt.figure()
for i in np.arange(len(y)):
    if y[i] < 0:
        plt.scatter(x[i][0], x[i][1], color='red')
    else:
        plt.scatter(x[i][0], x[i][1], color='blue')
x_test = np.array([4, 2])
plt.scatter(x_test[0], x_test[1], color='yellow')
plt.show()

distance = []
for i in range(len(x)):
    distance.append(math.sqrt((x_test[0]-x[i, 0])**2+(x_test[1]-x[i, 1])**2))

numpy_distance = np.array(distance)
# 返回排序后的索引 从小到大
index_sort_distance = np.argsort(numpy_distance)

k = 3
y_test = []
for i in range(k):
    y_test.append(y[index_sort_distance[i]])

print('predict result is:', y_test)

count_positive = 0
count_negative = 0

for i in range(len(y_test)):
    if y_test[i] == 1:
        count_positive += 1
    else:
        count_negative += 1
if count_positive> count_negative:
    print('belong to:', 1)
else:
    print('belong to:', -1)

