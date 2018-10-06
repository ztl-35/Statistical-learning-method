# 该文件用来计算所有数据各个分类的信息熵
from math import log
import operator

def calcShannongEntropy(dataset):
    # 定义数据集大小
    numEntries = len(dataset)
    # 定义标签中各个类别的数目
    label_Counts = {}
    # 统计各个类别中数目多少
    for featureVec in dataset:
        current_label = featureVec[-1]
        if current_label not in label_Counts.keys():
            label_Counts[current_label] = 0
        label_Counts[current_label] += 1

    ShannongEntropy = 0.0

    for key in label_Counts.keys():
        prob = float(label_Counts[key]) / numEntries
        ShannongEntropy -= prob * log(prob, 2)
    return ShannongEntropy

def splitDataSet(dataset, axis, value):
    retDataSet = []
    for featureVec in dataset:
        if featureVec[axis] == value:
            # reduceFeature是为了取出除了axis维度的值以外，保存这个向量中其他的值
            reduceFeature = featureVec[:axis]
            # 注意列表操作extend与append的区别
            reduceFeature.extend(featureVec[axis+1:])
            retDataSet.append(reduceFeature)
    return retDataSet

def chooseBestFeatureToSplit(dataset):
    numFeatures = len(dataset[0])-1
    baseEntropy = calcShannongEntropy(dataset)
    bestInfroGain = 0.0
    bestFeature = -1

    for i in range(numFeatures):
        # 每次取出的特征可能有多个重复的，需要去重
        featureList = [example[i] for example in dataset]
        uniqueFeatures = set(featureList)

        newEntropy = 0.0

        #计算在对应的特征下，所产生的信息熵的总和是多少。
        for value in uniqueFeatures:
            subDataset = splitDataSet(dataset, i, value)
            prob = len(subDataset) / float(len(dataset))
            newEntropy += prob * calcShannongEntropy(subDataset)

        # 对应特征下，信息增益的值是多少
        infroGain = baseEntropy - newEntropy

        # 更新迭代信息增益的取值
        if bestInfroGain < infroGain:
            bestInfroGain = infroGain
            bestFeature = i

    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createDataset():
    data_set = [[1, 1, 1, 'yes'], [1, 1, 0, 'yes'], [1, 0, 1, 'no'], [1, 1, 0, 'no'], [0, 1, 1, 'no'], [1, 0, 0, 'maybe']]

    # 代表的是特征的名称(表示上述dataset除了最后的标签之外剩余的值)
    labels = ['no surfacing', 'flippers', 'no flippers']

    return data_set,  labels
