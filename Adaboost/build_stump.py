import numpy as np
import data_process


# 与阈值进行比较，对应维度的值大于阈值，设为1，小于阈值。设为-10
def stump_classify(origin_data_matrix, dim, threshold, thresholdIneq):
    return_matrix = np.ones((np.shape(origin_data_matrix)[0], 1))
    # 对给定的阈值，到底是大于等于它是-1还是小于等于它是-1
    if thresholdIneq == 'lt':
        return_matrix[origin_data_matrix[:, dim] <= threshold] = -1.0
    else:
        return_matrix[origin_data_matrix[:, dim] > threshold] = 1.0
    return return_matrix

# 建立一个决策树桩，需要比较多个维度上的结果  构建了一个弱分类器：大于等于随机预测的结果q
def build_simple_stump(data_matrix, label, weight):
    # mat 函数生成与原对象相同地址， matrix生成一个在内存中全新的对象
    data_mat = np.mat(data_matrix)
    label_mat = np.mat(label).T
    m, n = np.shape(data_mat)
    num_steps = 10.0
    best_stumps = {}
    best_class = np.mat(np.zeros((m, 1)))
    min_error = np.inf

    #对所有特征进行遍历
    for i in range(n):
        range_min = data_mat[:, i].min()
        range_max = data_mat[:, i].max()
        step_size = (range_max - range_min)/num_steps
        # 在对应的特征值上进行遍历
        for j in range(-1, int(num_steps)+1):
            for inequal in ['lt', 'gt']:
                threshold_value = (range_min + step_size*float(j))
                predict_value = stump_classify(data_mat, i, threshold_value, inequal)
                error_array = np.mat(np.ones((m, 1)))

                # 将正确分类数据数组定为0
                error_array[predict_value == label_mat] = 0

                # 利用分错的权重的值相加--》相当于评价本次的分类效果
                weighted_error = weight.T * error_array

                if weighted_error < min_error:
                    min_error = weighted_error
                    best_class = predict_value.copy()
                    best_stumps['dim'] = i
                    best_stumps['threshold_value'] = threshold_value
                    best_stumps['inequal'] = inequal

    #     返回依次是最佳单层决策树信息，最小误差，原始数据最佳的预测分类
    return best_stumps, min_error, best_class
