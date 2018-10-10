from numpy import *
import math
import matplotlib.pyplot as plt
def loadDataSet():
    data_mat = []
    data_label = []
    test_file = open('testSet.txt')
    for line in test_file.readlines():
        line_array = line.strip().split()
        # 该行设置1.0的目的是为了之后的w*x计算方便 x0=1.0
        data_mat.append([1.0, float(line_array[0]), float(line_array[1])])
        data_label.append(int(line_array[2]))
    return data_mat, data_label

# sigmiod是分类器函数
def sigmiod(input_x):
    return 1.0/(1 + math.exp(-input_x))

# 全体数据迭代一次更新权重参数（一共迭代了500代）
def gradAscent(data_mat, data_label):
    data_matrix = np.mat(data_mat)
    # 转置 100*1
    data_class_label = np.mat(data_label).transpose()
    # 100*3
    m, n = np.shape(data_matrix)
    alpha = 0.001
    max_cycles = 500
    weights = np.ones((n, 1))
    for i in range(max_cycles):
        # 不是矩阵相乘，对应位置相乘 100*1
        temp_array = data_matrix * weights
        h = np.ones((m, 1))
        for j in range(m):
            h[j][0] = sigmiod(temp_array[j][0])
        error = data_class_label - h
        print('这是第几次训练: ', i, 'error: ', np.sum(error))
        # 梯度 = 数据的转置*误差
        gradient = data_matrix.transpose() * error
        weights = weights + alpha * gradient
    return weights


# 一次只用一个数据集样本更新权重，并且只更新1代 随机梯度上升
def stoc_grad_ascend(data_matrix, data_labels, epoch=5000):
    data_matrix = mat(data_matrix)
    m, n = shape(data_matrix)
    alpha = 0.001
    weights = ones((n, 1))
    plt.figure(1)

    for j in range(epoch):
        print('epoch: ',epoch)
        for i in range(m):
            h = sigmiod(sum(data_matrix[i]*weights))
            error = data_labels[i] - h
            weights = weights + alpha * error * data_matrix[i].transpose()
        plt.subplot(311)
        plt.scatter(j, weights[0].tolist())
        plt.subplot(312)
        plt.scatter(j, weights[1].tolist())
        plt.subplot(313)
        plt.scatter(j, weights[2].tolist())
    plt.show()
    plt.close()
    return weights

# 在随机梯度上升的基础上进行改进
def improve_stoc_grad_ascend(data_matrix, data_labels, epoch=5000):
    data_matrix = mat(data_matrix)
    m, n = shape(data_matrix)
    weights = ones((n, 1))
    plt.figure(1)

    for j in range(epoch):
        print('epoch: ', j)
        data_index = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + j + i)+0.01
            rand_index = int(random.uniform(0, len(data_index)))
            print('rand_index: ', rand_index)
            h = sigmiod(sum(data_matrix[rand_index]*weights))
            error = data_labels[rand_index] - h
            weights = weights + alpha * error * data_matrix[rand_index].transpose()
            del data_index[rand_index]
        plt.subplot(311)
        plt.scatter(j, weights[0].tolist())
        plt.subplot(312)
        plt.scatter(j, weights[1].tolist())
        plt.subplot(313)
        plt.scatter(j, weights[2].tolist())
    plt.show()
    plt.close()
    return weights