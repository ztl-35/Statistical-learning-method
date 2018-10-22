import numpy as np
import matplotlib.pyplot as plt
def load_simple_data():
    data = np.matrix([[1.0, 2.1],
                      [2.0, 1.1],
                      [1.3, 1.0],
                      [1.0, 1.0],
                      [2.0, 1.0]])
    class_labels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return data, class_labels

plt.figure()
data, label = load_simple_data()
data_label_1 = []
data_label_minus_1 = []
for i in range(len(label)):
    if label[i] == 1.0:
        data_label_1.append(data[i][:].tolist())
    else:
        data_label_minus_1.append(data[i][:].tolist())
data_label_1_x = []
data_label_1_y =[]
data_label_2_x = []
data_label_2_y =[]
for i in range(len(data_label_1)):
    data_label_1_x.append(data_label_1[i][0][0])
    data_label_1_y.append(data_label_1[i][0][1])
for i in range(len(data_label_minus_1)):
    data_label_2_x.append(data_label_minus_1[i][0][0])
    data_label_2_y.append(data_label_minus_1[i][0][1])
plt.plot(data_label_1_x, data_label_1_y, 'ro', label='positive sample')
plt.plot(data_label_2_x, data_label_2_y, 'b^', label='negative sample')


