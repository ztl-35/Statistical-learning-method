import split_word
import time

# 统计多项式贝叶斯所需的各个参数函数
def build_word():
    start = time.time()
    (spamMessage_word_base_list, origin_spam_words) = split_word.bulid_WordBase('spamMessage.xlsx')
    print('垃圾短信分词去重，去停用词后的数目： ', len(spamMessage_word_base_list))
    print('垃圾短信分词不去重，去停用词后的数目： ', len(origin_spam_words))

    (message_word_base_list, origin_message_words) = split_word.bulid_WordBase('message.xlsx')
    print('正常短信分词去重，去停用词后的数目: ', len(message_word_base_list))
    print('正常短信分词不去重，去停用词后的数目: ', len(origin_message_words))

    message_word_base_list[len(message_word_base_list):len(spamMessage_word_base_list)] = spamMessage_word_base_list
    word_base_list = list(set(message_word_base_list))
    end = time.time()
    print('建立词库表用时: ', (end - start), '秒')
    print('总词库表大小: ', len(word_base_list))

    # 多项式贝叶斯方法分母统计数目
    number_spam_allprocess = len(spamMessage_word_base_list)
    number_spam_not_Deduplication = len(origin_spam_words)
    number_normal_allprocess = len(message_word_base_list)
    number_normal_not_Deduplication = len(origin_message_words)

    # 多项式贝叶斯分子统计数目
    # 建立垃圾短信中在没有去重的情况下每个词的数目字典
    spam_word_dict = {}
    for i in range(len(origin_spam_words)):
        if origin_spam_words[i] in spam_word_dict.keys():
            spam_word_dict[origin_spam_words[i]] += 1
        else:
            spam_word_dict.update({origin_spam_words[i]: 1})

    # 建立正常短信中在没有去重的情况下每个词的数目字典
    normal_word_dict = {}
    for i in range(len(origin_message_words)):
        if origin_message_words[i] in normal_word_dict.keys():
            normal_word_dict[origin_message_words[i]] += 1
        else:
            normal_word_dict.update({origin_message_words[i]: 1})

    return len(word_base_list),number_spam_allprocess, number_spam_not_Deduplication, \
           number_normal_allprocess, number_normal_not_Deduplication, \
           spam_word_dict, normal_word_dict






