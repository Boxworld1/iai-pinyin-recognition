import string
import pickle

def main():
    chn2num = {}
    num2chn = {}
    # 汉字编号由 1 开始
    cnt = 1

    # 读入一二级汉字表
    with open("../raw_data/hanzilist.txt", encoding="gbk") as inputFile:
        
        dataset = inputFile.readlines()

        for i in range(len(dataset)):
            str = dataset[i]
            for j in range(len(str)):
                # 对每一个汉字编号
                chn2num[str[j]] = cnt
                num2chn[cnt] = str[j]
                cnt += 1

        # 建立汉字-数字表
        outputFile = open('./pretrained_data/hanzimap.txt','wb')
        pickle.dump(chn2num, outputFile)
        outputFile.close()

        # 建立数字-汉字表
        outputFile = open('./pretrained_data/hanzidecode.txt','wb')
        pickle.dump(num2chn, outputFile)
        outputFile.close()
    
if __name__ == "__main__":
    print("Running gen_chi_map.py ...")
    main()
    print("Finished running gen_chi_map.py")
    print()