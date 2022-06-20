import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-gc", "--gen_pinyin_hanzi_list", action="store_true", help="拼音、一二级汉字预处理")
    parser.add_argument("-gf", "--get_frequency", action="store_true", help="统计基础语料库对应汉字频率")
    parser.add_argument("-gfb", "--get_frequency_both", action="store_true", help="统计基础与维基语料库对应汉字频率")
    parser.add_argument("-r", "--run", default="false", help="运行模型。可选值为：normal_2.py, normal_3.py, normal_23.py, smooth_2.py, smooth_3.py")
    parser.add_argument("-d", "--data", default="pretrained_data", help="选定语料库。可选值为：pretrained_data, pretrained_data_with_wikipedia")
    parser.add_argument("-c", "--compare", action="store_true", help="对比输出文件")
    parser.add_argument("-if", "--inputfile", default="../data/input.txt", help="指定输入文件的位置")
    parser.add_argument("-of", "--outputfile", default="../data/output.txt", help="指定输出文件的位置")
    parser.add_argument("-sf", "--sourcefile", default="../data/std_output.txt", help="指定对比文件的位置")
    args = parser.parse_args()

    print("---------------- Start  process ----------------")
    print()
    if args.gen_pinyin_hanzi_list:
        os.system("python3 gen_chi_map.py")
        os.system("python3 gen_pinyin_list.py")

    if args.get_frequency_both:
        os.system("python3 get_freq_wikipedia.py")
    elif args.get_frequency:
        os.system("python3 get_freq_sina.py")
    
    if args.run != "false":
        cmd = "python3 " + args.run
        if args.inputfile:
            cmd = cmd + " -if " + args.inputfile
        if args.outputfile:
            cmd = cmd + " -of " + args.outputfile
        if args.data:
            cmd = cmd + " -d " + args.data
        os.system(cmd)

        cmd2 = "python3 compare.py"
        if args.outputfile:
            cmd2 = cmd2 + " -of " + args.outputfile
        if args.sourcefile:
            cmd2 = cmd2 + " -sf " + args.sourcefile

        os.system(cmd2)

    if args.compare:
        cmd2 = "python3 compare.py"
        if args.outputfile:
            cmd2 = cmd2 + " -of " + args.outputfile
        if args.sourcefile:
            cmd2 = cmd2 + " -sf " + args.sourcefile

        os.system(cmd2)

    print("---------------- Finish process ----------------")

if __name__ == "__main__":
    main()