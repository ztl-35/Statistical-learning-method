import compute_parameter
import inverted_index

test_txt = '新年好,苏州和无锡集团喜洋洋'
split_word_test_txt = inverted_index.split_words(test_txt)
split_result = split_word_test_txt.split(" ")
split_result.remove('')

# 加载参数列表
(normal_word_probility, spam_word_probility) = compute_parameter.compute_para()

#
# 计算属于每个类别的概率

# 每个类别的数据数目概率
probility_normal = 0.9
probility_spam = 0.1

# 计算属于正常文档的概率
for i in range(len(split_result)):
    key = split_result[i]
    if key in normal_word_probility.keys():
        probility_normal = probility_normal * normal_word_probility[key]
    else:
        # 计算测试集中的词不在训练集中出现的情况
        probility_normal = probility_normal * 1/(90000+2)

# 计算训练集中其他词没有出现在测试集中的概率
for key in normal_word_probility:
    value = normal_word_probility[key]
    if key in split_result:
        pass
    else:
        probility_normal = probility_normal * (1-value)
# ****************************************************************************
# 计算属于垃圾文档的概率
for i in range(len(split_result)):
    key = split_result[i]
    if key in spam_word_probility.keys():
        probility_spam = probility_spam * spam_word_probility[key]
    else:
        # 计算测试集中的词不在训练集中出现的情况
        probility_spam = probility_spam * 1 / (10000 + 2)

# 计算训练集中其他词没有出现在测试集中的概率
for key in spam_word_probility:
    value = spam_word_probility[key]
    if key in split_result:
        pass
    else:
        probility_spam = probility_spam * (1 - value)
# ****************************************************************************
print('属于正常文档的概率是：  ', probility_normal)
print('属于垃圾文档的概率是：  ', probility_spam)

print('*'*30)
if probility_spam > probility_normal:
    print('该测试文档属于垃圾短信')
else:
    print('该测试文档属于正常短信')

