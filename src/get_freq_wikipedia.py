import string
import json
import pickle
import re
import os
from pathlib import Path

chi2num = {}
numb = {"0": "零", "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九"}

# 汉字转数字
def c2n(chr):
    tmp = 0
    # 数字转汉字，效果不佳，此处不使用
    # if chr in numb:
    #     chr = numb[chr]

    if chr in chi2num:
        tmp = chi2num[chr]
    return tmp

# 汉字插入字典   
def add(myDict, id, var):
    if id in myDict:
        myDict[id] += var
    else:
        myDict[id] = var


def main():
    global chi2num

    wordcount = int(6764)

    # 读入汉字-数字对应表
    inputFile = open("./pretrained_data/hanzimap.txt", "rb")
    chi2num = pickle.load(inputFile)
    inputFile.close()

    frequencyF = {}
    frequency1 = {}
    frequency2 = {}
    frequency3 = {}

    pathlist = Path("../raw_data/corpus").glob("**/**/*")

    for path in pathlist:

        # 不考虑奇怪的文件
        if path.name ==".DS_Store":
            continue

        # 跳过文件夹
        if os.path.isdir(path):
            continue

        # 默认使用 UTF-8 解码
        encode = "utf8"
        body = "text"

        # 新浪语料的结尾为 txt，维基语料无后缀名
        if path.suffix == ".txt":
            encode = "gbk"
            body = "html"

        # 显示当前读入的文件
        print("  Reading \"", end="")
        print(path, end="")
        print("\" with " + encode)
        

        inputFile = open(path, encoding=encode)
        
        dataset = inputFile.readlines()

        for i in range(len(dataset)):
            myJson = json.loads(dataset[i])

            # 提取有用的部分
            title = myJson["title"]
            html = myJson[body]

            # 以各种符号断句
            strList = re.split("，|。|”|“|\"|：|；|（|）|\n| |《|》", title + " " + html)

            for str in strList:

                if len(str) <= 0:
                    continue

                # 首字符分开讨论
                last = c2n(str[0])
                last2 = 0
                add(frequency1, 0, 1)
                add(frequencyF, 0, 1)
                add(frequency1, last, 1)
                add(frequencyF, last, 1)

                # 其他字符
                for chr in str:
                    now = c2n(chr)

                    if now > 0:
                        add(frequency1, 0, 1)
                        add(frequency1, now, 1)
                        
                        # 连续两字符
                        if last > 0:
                            add(frequency2, 0, 1)
                            add(frequency2, last * wordcount + now, 1)
                            
                            # 连续三字符
                            if last2 > 0:
                                add(frequency3, 0, 1)
                                add(frequency3, last2 * wordcount * wordcount + last * wordcount + now, 1)

                    last2 = last
                    last = now

                
        inputFile.close()
        print("  Finished reading ")
        print(path)

    # 生成统计文件
    outputFile = open('./pretrained_data_with_wikipedia/frequencyF.txt','wb')
    pickle.dump(frequencyF, outputFile)
    outputFile.close()

    outputFile = open('./pretrained_data_with_wikipedia/frequency1.txt','wb')
    pickle.dump(frequency1, outputFile)
    outputFile.close()
        
    outputFile = open('./pretrained_data_with_wikipedia/frequency2.txt','wb')
    pickle.dump(frequency2, outputFile)
    outputFile.close()

    outputFile = open('./pretrained_data_with_wikipedia/frequency3.txt','wb')
    pickle.dump(frequency3, outputFile)
    outputFile.close()

if __name__ == "__main__":
    print("Running gen_freq_wikipedia.py ...")
    main()
    print("Finished running gen_freq_wikipedia.py")
    print()