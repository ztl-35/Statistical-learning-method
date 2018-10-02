from multinomial_Bayes import My_Bayes
import split_word

(number_total_word, number_spam_allprocess, number_spam_not_Deduplication,
    number_normal_allprocess, number_normal_not_Deduplication,
    spam_word_dict, normal_word_dict) = My_Bayes.build_word()

test_txt = '新年好,苏州和无锡集团喜洋洋'
split_test_txt = split_word.split_words(test_txt)
split_test_txt_list = split_test_txt.split(" ")
split_test_txt_list.remove('')

# 初始化概率是短信的数据量比
spam_probility = 0.1
normal_probility = 0.9
for i in range(len(split_test_txt_list)):
    temp_string = split_test_txt_list[i]
    if temp_string in normal_word_dict.keys():
        normal_probility = normal_probility * ((normal_word_dict[temp_string]+1)/(number_normal_not_Deduplication+number_total_word))
    else:
        # 如果测试集中的词不在训练集中出现，需要进行默认概率的计算
        normal_probility = normal_probility * (1/(number_normal_not_Deduplication+ number_total_word))
    if temp_string in spam_word_dict.keys():
        spam_probility = spam_probility * ((spam_word_dict[temp_string]+1)/(number_spam_not_Deduplication+number_total_word))
    else:
        spam_probility = spam_probility * (1/(number_spam_not_Deduplication+number_total_word))

print('*'*30)
print('垃圾短信的概率： ', spam_probility)
print('正常短信的概率：', normal_probility)

print('*'*30)
if spam_probility > normal_probility:
    print('这条测试集属于垃圾短信')
else:
    print('这条测试集属于正常短信')