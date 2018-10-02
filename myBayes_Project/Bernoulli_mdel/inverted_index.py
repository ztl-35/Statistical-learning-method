# 本文件用来建立贝努利模型的每个词的倒排索引列表

import xlrd
import jieba

def stopWordsList():
    stopwords = [line.strip() for line in open('stopwords.txt').readlines()]
    return stopwords

# 对句子进行分词
def split_words(sentence):
    if type(sentence) == int:
        return 0
    split_words = jieba.cut(sentence)

    # 停用词处理
    stopword = stopWordsList()

    # 保存输出结果
    outstr = ''

    for word in split_words:
        if word not in stopword:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

def build_invert_index(ExcelFileName):
    excel_file = xlrd.open_workbook(ExcelFileName)
    sheet = excel_file.sheet_by_index(0)

    # 建立倒排索引字典
    invert_index_dict = {}

    for i in range(sheet.nrows):
        split_txt = split_words(sheet.cell(i, 2).value)
        if split_txt == 0:
            continue
        split_result = split_txt.split(" ")
        split_result.remove('')

        final_result = []
        for j in range(len(split_result)):
            split_word = split_result[j]
            flag = True
            for ch in split_word:
                # 分词过后有部分可能出现是数字或者其他乱码字符，现在统一删除形成中文词库表
                if '\u4e00' <= ch <= '\u9fff':
                    continue
                else:
                    flag = False
                    break
            if flag:
                final_result.append(split_word)

        for j in range(len(final_result)):
            temp_string = final_result[j]
            if temp_string in invert_index_dict.keys():
                # i+1是真正的文档序号
                invert_index_dict[temp_string].append(i+1)
            else:
                invert_index_dict[temp_string] = [i+1]

    return invert_index_dict




