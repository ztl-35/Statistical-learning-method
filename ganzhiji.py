import numpy as np
import math
import matplotlib.pyplot as plt
x = np.array([[1, 0.5],
              [2, 0.5],
              [3, 0.5],
              [3, 4.7],
              [4, 4],
              [5, 4.5],
              [6, 3.1],
              [5, 1],
              [4, -0.1],
              [4, -1]])

y = np.array([-1, -1, -1, -1, 1, 1, 1, 1, 1, 1])
plt.figure()
for i in np.arange(len(y)):
    if y[i] < 0:
        plt.scatter(x[i][0], x[i][1], color='red')
    else:
        plt.scatter(x[i][0], x[i][1], color='blue')

# 设定初值
w0 = np.array([0, 0]).reshape((1, 2))
b0 = 0
yeta = 1

flag = False
while(not flag):
    for i in range(len(y)):
        xi = x[i, :]
        yi = y[i]
        if yi * (np.dot(w0, np.transpose(xi))+ b0) <= 0:
            w0 = w0 + yeta * np.dot(yi, xi)
            b0 = b0 + yeta * yi
            flag = False
            print('正在训练。。。')
            break
        if i == (len(y)-1):
            print('训练完毕。。。')
            flag = True
            break
xx = np.linspace(0, 5, 50)

yy = -w0[0, 0]/w0[0, 1] * xx - (b0/w0[0, 1])
plt.plot(xx, yy)

sum = 0
for i in range(len(y)):
    xi = x[i, :]
    print('第', i, '个点的感知机结果是：', (np.dot(w0, np.transpose(xi))+b0))
    sum = sum + math.fabs(np.dot(w0, np.transpose(xi)) + b0)/(math.sqrt((w0[0, 0]**2 + w0[0, 1]**2)))
print('训练结束 误差是:', sum)
plt.show()


