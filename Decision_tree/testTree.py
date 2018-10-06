import plotTree
import createDecisionTree
import computePara

if __name__ == '__main__':
    data_set, labels = computePara.createDataset()
    origin_labels = labels.copy()
    decision_tree = createDecisionTree.createTree(data_set, labels)
    test_label = createDecisionTree.classify(decision_tree, origin_labels, [1, 0, 1])
    print('该测试向量属于的类别是： ', test_label)
    plotTree.createPlot(decision_tree)


