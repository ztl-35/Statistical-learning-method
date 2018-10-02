import inverted_index

def compute_para():
    print('*'*30)
    print('开始建立倒排文档。。。')
    normal_invert_index = inverted_index.build_invert_index(r'message.xlsx')
    spam_invert_index = inverted_index.build_invert_index(r'spamMessage.xlsx')
    print('倒排文档建立完毕...')
    print('*' * 30)
    normal_document_number = 90000
    spam_document_number = 10000
    message_class = 2

    normal_word_probility = {}
    spam_word_probility = {}

    # 计算正常短信词的概率
    for key in normal_invert_index:
        value = normal_invert_index[key]
        if (len(value) + 1)/(normal_document_number + message_class) >= 1:
            normal_word_probility[key] = 1 / (normal_document_number + message_class)
        else:
            normal_word_probility[key] = (len(value) + 1)/(normal_document_number + message_class)
    # 计算垃圾短信词的概率
    for key in spam_invert_index:
        value = spam_invert_index[key]
        # 对于概率计算大于1的值，那么它在文件中出现的次数太多，在这里直接进行默认最小概率计算（这种词其实在停用词表中应该直接去除）
        if (len(value) + 1)/(spam_document_number + message_class) >= 1:
            spam_word_probility[key] = 1 / (spam_document_number + message_class)
        else:
            spam_word_probility[key] = (len(value) + 1)/(spam_document_number + message_class)
    return normal_word_probility, spam_word_probility

