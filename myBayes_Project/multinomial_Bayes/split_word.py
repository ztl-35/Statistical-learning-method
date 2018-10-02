import jieba
import xlrd
# 创建停用词表列

def stopWordsList():
    stopwords = [line.strip() for line in open('stopwords.txt').readlines()]
    return stopwords

# 对句子进行分词
def split_words(sentence):
    if(type(sentence) == int):
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

def build_Base(ExcelFileName):
    ExcelFile = xlrd.open_workbook(ExcelFileName)
    sheet = ExcelFile.sheet_by_index(0)
    wordBaseList= []
    for i in range(sheet.nrows):
        split_txt = split_words(sheet.cell(i, 2).value)
        if(split_txt == 0):
            continue
        split_result = split_txt.split(" ")
        split_result.remove('')
        wordBaseList[len(wordBaseList): len(split_result)] = split_result
#     列表函数set()去重
    origin_word_number = wordBaseList
    wordBaseList = list(set(wordBaseList))
    return wordBaseList, origin_word_number

def bulid_WordBase(Excel_File_Name):
    print('starting split word...')
    (result, origin_temp_word_number) = build_Base(Excel_File_Name)
    print('stop split word...')

    final_result = []
    origin_word_number = []
    for i in range(len(result)):
        split_word = result[i]
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

    for i in range(len(origin_temp_word_number)):
        split_word = origin_temp_word_number[i]
        flag = True
        for ch in split_word:
            # 分词过后有部分可能出现是数字或者其他乱码字符，现在统一删除形成中文词库表
            if '\u4e00' <= ch <= '\u9fff':
                continue
            else:
                flag = False
                break
        if flag:
            origin_word_number.append(split_word)
    return final_result, origin_word_number