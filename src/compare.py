import argparse

file1 = "../data/output.txt"
file2 = "../data/std_output.txt"

def get_args():
    global file1, file2
    parser = argparse.ArgumentParser()
    parser.add_argument("-of", "--outputfile", default="../data/output.txt", help="指定输出文件的位置")
    parser.add_argument("-sf", "--sourcefile", default="../data/std_output.txt", help="指定对比文件的位置")
    args = parser.parse_args()
    file1 = args.sourcefile
    file2 = args.outputfile
    print("  Source file: \"" + file1 + "\"")
    print("  Output file: \"" + file2 + "\"")

def main():
    # 读入命令行参数
    get_args()

    global file1, file2
    # 读入待测试文件
    inputFile = open(file1, "r")
    file1 = inputFile.readlines()
    inputFile.close()

    inputFile = open(file2, "r")
    file2 = inputFile.readlines()
    inputFile.close()

    # 统计数据
    cntWordCorrect = 0
    cntWord = 0
    cntSentenceCorrect = 0
    cntSentence = 0

    # 按行对比
    for i in range(len(file1)):
        flag = True
        str1 = file1[i]
        str2 = file2[i]
        
        # 按行中每一个字对比
        for j in range(len(str1)):
            cntWord += 1
            if str1[j] == str2[j]:
                cntWordCorrect += 1
            else:
                flag = False
        
        cntSentence += 1

        # 若两字串完全相同
        if flag == True:
            cntSentenceCorrect += 1

    print("  Word Accuracy: ", cntWordCorrect / cntWord)
    print("  Sentence Accuracy: ", cntSentenceCorrect / cntSentence)


if __name__ == "__main__":
    print("Running compare.py ...")
    main()
    print("Finished running compare.py")
    print()