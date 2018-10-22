import data_process
import build_stump
import numpy as np
import matplotlib.pyplot as plt
def my_adaboost(data_matrix, label, num_iteration):
    adabosot_function_list = []
    N = np.shape(data_matrix)[0]
    # 初始化权重向量
    weight = np.ones((N, 1)) / N

    # 初始化分类结果
    agg_class = np.mat(np.ones((N, 1)))

    for m in range(num_iteration):
        print('****************************')
        print('m: ', m)
        # 得到基本分类器
        best_stumps, error, best_class = build_stump.build_simple_stump(data_matrix, label, weight)
        print('weight matrix: ', weight.T)
        print('single tree best_class: ', best_class)

        #计算函数的权重系数
        gmx_weight = 0.5 * np.log((1-error)/max(error, 1e-16))
        best_stumps['alpha'] = gmx_weight
        adabosot_function_list.append(best_stumps)

        #更新训练集权重分布值

        expon = np.multiply(-1*gmx_weight.tolist()[0][0]*np.mat(label).T, best_class)
        weight = np.multiply(weight, np.exp(expon))/weight.sum()
#       计算累计错误率
        agg_class += gmx_weight.tolist()[0][0]*best_class

        # 不等于号出来的结果是TRUE或者FALSE，通过与ones矩阵相乘，转化为数值矩阵
        agg_errors = np.multiply(np.sign(agg_class) != np.mat(label).T, np.ones((N, 1)))
        error_rate = agg_errors.sum() / N
        print('total error: ', error_rate)
        if error_rate == 0.0:
            break
    return adabosot_function_list


def adaClassify(predict_data, classify_array):
    data_matrix = np.mat(predict_data)
    m = np.shape(data_matrix)[0]
    agg_classify = np.mat(np.zeros((m, 1)))

    for i in range(len(classify_array)):
        class_result = build_stump.stump_classify(data_matrix,
                                                  classify_array[i]['dim'],
                                                  classify_array[i]['threshold_value'],
                                                  classify_array[i]['inequal'])
        print('1: ',classify_array[i]['alpha'],' 2: ', class_result)
        agg_classify += classify_array[i]['alpha'].tolist()[0][0]*class_result
    return np.sign(agg_classify)

data, label = data_process.load_simple_data()
class_array = my_adaboost(data, label, 50)
print('predict result; ', adaClassify([[0, 0], [5, 5]], class_array))

plt.plot([0, 5], [0, 5], 'yo', label='predict result')
plt.legend(loc='upper left')
plt.show()








