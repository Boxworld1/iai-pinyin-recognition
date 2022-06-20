import string
import json
import pickle
import re

chi2num = {}

# 汉字转数字
def c2n(chr):
    tmp = 0
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
    month = ["02", "04", "05", "06", "07", "08", "09", "10", "11"]

    # 读入汉字-数字对应表
    inputFile = open("./pretrained_data/hanzimap.txt", "rb")
    chi2num = pickle.load(inputFile)
    inputFile.close()

    frequencyF = {}
    frequency1 = {}
    frequency2 = {}
    frequency3 = {}

    # 按月份读入
    for mo in month:
        myFilename = "../raw_data/corpus/sina_news_gbk/2016-" + mo + ".txt"
        inputFile = open(myFilename, encoding="gbk")
        print("  Reading \"" + myFilename + "\" ...")

        dataset = inputFile.readlines()

        # 遍历数据
        for i in range(len(dataset)):
            myJson = json.loads(dataset[i])

            # 提取有用的部分
            title = myJson["title"]
            html = myJson["html"]

            # 断句
            strList = re.split("，|。|”|“|：|；|（|）| ", title + " " + html)

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
        print("  Finished reading \"" + myFilename + "\"")

    # 生成统计文件
    outputFile = open('./pretrained_data/frequencyF.txt','wb')
    pickle.dump(frequencyF, outputFile)
    outputFile.close()

    outputFile = open('./pretrained_data/frequency1.txt','wb')
    pickle.dump(frequency1, outputFile)
    outputFile.close()
        
    outputFile = open('./pretrained_data/frequency2.txt','wb')
    pickle.dump(frequency2, outputFile)
    outputFile.close()

    outputFile = open('./pretrained_data/frequency3.txt','wb')
    pickle.dump(frequency3, outputFile)
    outputFile.close()

if __name__ == "__main__":
    print("Running gen_freq_sina.py ...")
    main()
    print("Finished running gen_freq_sina.py")
    print()