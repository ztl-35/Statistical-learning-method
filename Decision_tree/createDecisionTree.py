import computePara

def createTree(data_set, labels):
    # 计算所有的标签列表
    class_list = [example[-1] for example in data_set]

    # 递归终止条件
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(data_set[0]) == 1:
        return computePara.majorityCnt(class_list)

    bestFeature = computePara.chooseBestFeatureToSplit(data_set)
    bestFeatureLable = labels[bestFeature]

    myTree = {bestFeatureLable: {}}
    del labels[bestFeature]

    featureVec = [example[bestFeature] for example in data_set]
    uniqueFeatureVals = set(featureVec)

    for value in uniqueFeatureVals:
        subLabels = labels[:]
        myTree[bestFeatureLable][value] = createTree(computePara.splitDataSet(data_set, bestFeature, value), subLabels)
    return myTree

def classify(inputTree, feature_label, testVec):
    firstStr = list(inputTree.keys())[0]
    # 根节点下的树数据
    secondDict = inputTree[firstStr]
    # 将标签字符串转换为索引

    featureIndex = feature_label.index(firstStr)

    class_label = -1
    for key in secondDict.keys():
        if testVec[featureIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                class_label = classify(secondDict[key], feature_label, testVec)
            else:
                class_label = secondDict[key]
    return class_label
