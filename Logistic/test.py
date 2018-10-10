import Gradient_Rise
import matplotlib.pyplot as plt
import numpy as np
def plot_fit():
    data_mat, data_label = Gradient_Rise.loadDataSet()

    weights = Gradient_Rise.improve_stoc_grad_ascend(data_mat, data_label)

    plt.figure(2)
    m, n = np.shape(data_mat)
    for i in range(m):
        if data_label[i] == 1:
            plt.scatter(data_mat[i][1], data_mat[i][2], c='red')
        else:
            plt.scatter(data_mat[i][1], data_mat[i][2], c='green')

    x = np.arange(-5, 5, 0.01)
    y = ((-weights[0]-weights[1]*x)/weights[2]).transpose()
    plt.plot(x, y)
    plt.show()
plot_fit()