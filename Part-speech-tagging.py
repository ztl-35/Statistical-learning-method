import numpy as np
# 记录所有可能出现的词性
def count_tagging_and_words(file_name):
    # （1）所有可能的词性。
    #
    # （2）所有出现的词语。
    tag_list = []
    word_list = []
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            else:
                line = line.split("  ")
                for i in range(len(line)):
                    # 月份这个部分全部舍弃
                    if i == 0:
                        continue
                    else:
                        temp_line = line[i]
                        # [全国/n', '工商联/j]nt 这种类型不做处理
                        if "[" in temp_line or "]" in temp_line:
                            continue
                        temp_word_tag = temp_line[line[i].find("/"):]
                        temp_word = temp_line[0: line[i].find("/")]

                        if temp_word not in word_list:
                            word_list.append(temp_word)
                        else:
                            pass

                        if temp_word_tag not in tag_list:
                            tag_list.append(temp_word_tag)
                        else:
                            pass
    return tag_list, word_list

def function_count(file_name):
    # （3）每个词语以不同词性出现的次数。
    #
    # （4）记录句首词为不同词性的次数。
    #
    # （5）记录句子中任一两种词性相邻的次数
    tag_list, word_list = count_tagging_and_words(file_name)

    # 初始化每个词语对应的词性出现的个数为0
    word_tag = {}
    for i in range(len(tag_list)):
        word_tag[tag_list[i]] = {}
        for j in range(len(word_list)):
            word_tag[tag_list[i]][word_list[j]] = 0

    # 首词统计初始化为0
    first_tag = {}
    for i in range(len(tag_list)):
        first_tag[tag_list[i]] = 0

    # 初始化任一两种词性出现的次数
    two_tag = {}
    for i in range(len(tag_list)):
        two_tag[tag_list[i]] = {}
        for j in range(len(tag_list)):
            two_tag[tag_list[i]][tag_list[j]] = 0

    with open(file_name, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            else:
                line = line.split("  ")
                for i in range(len(line)):
                    # 月份这个部分全部舍弃
                    if i == 0:
                        continue
                    else:
                        temp_line = line[i]
                        tag = temp_line[line[i].find("/"):]
                        word = temp_line[0: line[i].find("/")]

                        if i == 1:
                            # 首词词性统计
                            first_tag[tag] += 1

                        # 每个词性对应的不同词语出现的次数
                        word_tag[tag][word] += 1

                        if i < (len(line) - 1):
                            next_line = line[i+1]
                            next_tag = next_line[next_line.find("/"):]
                            two_tag[tag][next_tag] += 1
                        else:
                            # 如果已经是最后一个词，就不统计，直接pass
                            pass
    return word_tag, first_tag, two_tag

def cal_possibility(file_name):

    word_tag, first_tag, two_tag = function_count(file_name)

    # 首词出现比率
    sum_frequence_tag = 0
    for key, value in first_tag.items():
       sum_frequence_tag += value
    for key, value in first_tag.items():
        # 全部转换成概率
        if value == 0:
            first_tag[key] = 1 / sum_frequence_tag
        else:
            first_tag[key] = value / sum_frequence_tag

    # 全部词性转换变成概率
    sum_tag = np.zeros([len(first_tag)])
    for key, value in two_tag.items():
        count = 0
        for key1, value1 in value.items():
            sum_tag[count] += value1
            count += 1
    for key, value in two_tag.items():
        count = 0
        for key1, value1 in value.items():
            if sum_tag[count] == 0:
                sum_tag[count] = 1
            two_tag[key][key1] = value1 / sum_tag[count]
            count += 1

    # 计算发射概率
    sum_word = []
    for tag, word_dic in word_tag.items():
        word_count = 0
        for word, word_num in word_dic:
            word_count += word_num
        sum_word.append(word_count)

    for tag, word_dic in word_tag.items():
        index = 0
        for word, word_num in word_dic:
            if sum_word[index] == 0:
                sum_word[index] = 1
            word_tag[tag][word] = word_num / sum_word[index]
        index += 1

    # 对应的是 初始概率，发射概率， 转移概率
    return first_tag, word_tag, two_tag

if __name__ == '__main__':

    print("正在训练...")
    first_tag, word_tag, two_tag = cal_possibility("yuliao.txt")
    print("训练完毕...")

    split_word_tag = input("请输入你需要进行标注的分词语句,用逗号分隔...")
    split_word_tag_list = split_word_tag.split(",")


    delta = {}
    for i in range(len(split_word_tag_list)):
        delta[i] = {}
        for key, value in first_tag.items():
            delta[i][key] = 0
    fa = {}
    for i in range(len(split_word_tag_list)):
        fa[i] = {}
        for key, value in first_tag.items():
            fa[i][key] = ""

    # 初始化
    for tag, tag_first_value in first_tag.items():
        temp = tag_first_value * word_tag[tag][split_word_tag_list[0]]
        delta[0][tag] = temp
        fa[0][tag] = "start"


    # 递推
    for t in np.arange(1, len(split_word_tag_list), 1):

        # i
        for tag, tag_first_value in first_tag.items():
            max = 0
            cixing = ''
            # j
            for tag1, tag_first_value1 in first_tag.items():
                temp = delta[t-1][tag1] * two_tag[tag1][tag]
                if temp > max:
                    max = temp
                    cixing = tag1

            fa[t][tag] = cixing
            delta[t][tag] = max * word_tag[tag][split_word_tag_list[t]]
    # 终止
    p_start = 0
    cixing = ""
    for key, value in first_tag.items():
        if delta[len(split_word_tag_list)-1][key] > p_start:
            p_start = delta[len(split_word_tag_list)-1][key]
            cixing = key

    # 最优路径回溯
    result = []
    for t in np.arange(len(split_word_tag_list)-2, 1, 1):
        temp = fa[t+1][cixing]
        result.append(temp)
    print("预测的词性是: ")
    for i in range(len(result)):

        print("第", i, "个词性是： ", result[i])
    print("最后一个词性是：", cixing)
