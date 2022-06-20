import string
import pickle

def main():
    myDict = {}

    # 读入拼音-汉字表
    with open("../raw_data/pinyinlist.txt", encoding="gbk") as inputFile:
        
        # 以行读入
        dataset = inputFile.readlines()

        # 遍历行中元素
        for i in range(len(dataset)):
            str = dataset[i]

            # 以空格分开
            myList = str.split()

            # 取出拼音，并在列表中删去
            key = myList[0]
            del myList[0]

            # 将剩余汉字插入字典中
            myDict[key] = myList

        outputFile = open('./pretrained_data/pinyinlist.txt','wb')
        pickle.dump(myDict, outputFile)
        outputFile.close()
    
if __name__ == "__main__":
    print("Running gen_pinyin_list.py ...")
    main()
    print("Finished running gen_pinyin_list.py")
    print()