import numpy as np

def createData(k, mu, sigma, dataNum):
    data = []
    for i in range(len(k)):
        data += np.random.normal(mu[i], sigma[i], int(k[i] * dataNum)).tolist()
    return data

def generateData(k,mu,sigma,dataNum):
    '''
    产生混合高斯模型的数据
    :param k: 比例系数
    :param mu: 均值
    :param sigma: 标准差
    :param dataNum:数据个数
    :return: 生成的数据
    '''
    # 初始化数据
    dataArray = np.zeros(dataNum,dtype=np.float32)
    # 逐个依据概率产生数据
    # 高斯分布个数
    n = len(k)
    for i in range(dataNum):
        # 产生[0,1]之间的随机数
        rand = np.random.random()
        Sum = 0
        index = 0
        while(index < n):
            Sum += k[index]
            if(rand < Sum):
                dataArray[i] = np.random.normal(mu[index],sigma[index])
                break
            else:
                index += 1
    print('data: ', dataArray)
    return dataArray

def normPdf(x, mu, sigma):
    return 1/(sigma * np.sqrt(2 * np.pi))*np.exp(-(x - mu)**2/(2*sigma**2))

def em(dataArray,k,mu,sigma,step = 10):
    n = len(k)
    # 数据个数
    dataNum = len(dataArray)
    # 初始化gama数组
    gamaArray = np.zeros((n, dataNum))
    for s in range(step):
        for i in range(n):
            for j in range(dataNum):
                Sum = sum([k[t]*normPdf(dataArray[j],mu[t],sigma[t]) for t in range(n)])

                gamaArray[i][j] = k[i]*normPdf(dataArray[j],mu[i],sigma[i])/float(Sum)
        # 更新 mu
        for i in range(n):
            mu[i] = np.sum(gamaArray[i]*dataArray)/np.sum(gamaArray[i])
        # 更新 sigma
        for i in range(n):
            sigma[i] = np.sqrt(np.sum(gamaArray[i]*(dataArray - mu[i])**2)/np.sum(gamaArray[i]))
        # 更新系数k
        for i in range(n):
            k[i] = np.sum(gamaArray[i])/dataNum

    return [k,mu,sigma]


def Em(data_arr, k, mu, sigma, step = 10):
    k_num = len(k)

    data_num = len(data_arr)

    # Expectation step
    #     initial gama array
    gama_arr = np.zeros((k_num, data_num))
    for epoch in range(step):
        for i in range(k_num):
            for j in range(dataNum):
                Sum = sum([k[t]*normPdf(data_arr[j], mu[t], sigma[t]) for t in range(k_num)])
                gama_arr[i][j] = k[i]*normPdf(data_arr[j], mu[i], sigma[i])/float(Sum)
        # maximum step

        # update mu
        for kk in range(k_num):
            mu[kk] = np.sum(gama_arr[kk] * data_arr)/np.sum(gama_arr[kk])

        # update sigma
        for kk in range(k_num):
            sigma[kk] = np.sqrt(np.sum(gama_arr[kk]*(data_arr-mu[kk])**2) / np.sum(gama_arr[kk]))

        # update k
        for kk in range(k_num):
            k[kk] = np.sum(gama_arr[kk]) / data_num
    return [k, mu, sigma]


if __name__ == '__main__':
    # 参数的准确值
    k = [0.3, 0.4, 0.3]
    mu = [2, 4, 3]
    sigma = [1, 1, 4]
    # 样本数
    dataNum = 5000
    data = createData(k, mu, sigma, dataNum)
    # 将3个一维的高斯混合模型产生的数据通过shuffle操作，变成一个高斯混合模型的原始数据
    np.random.shuffle(np.array(data))

    # em initial parameter
    k0 = [0.3, 0.3, 0.4]
    mu0 = [1, 2, 2]
    sigma0 = [1, 1, 1]
    print('original result:')
    print('k: ', k0, ' mu: ', mu0, ' sigma: ', sigma0)
    step = 100
    k, mu, sigma = Em(data, k0, mu0, sigma0, step)

    print('predict result:')
    print('k: ', k, ' mu: ', mu, ' sigma: ', sigma)



