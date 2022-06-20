# 模型使用方法



**请确保你是在文件根目录下开启命令行，然后在命令行输入：**

```
cd src
python3 main.py -h
```

这时你应该看到：

| 命令 | 参数                                    | 用途                               |
| ---- | --------------------------------------- | ---------------------------------- |
| -gc  | 无                                      | 拼音、一二级汉字预处理             |
| -gf  | 无                                      | 统计新浪语料库对应汉字频率         |
| -gfb | 无                                      | 统计新浪与维基语料库对应汉字频率   |
| -r   | 对应模型文件                            | 运行模型并对比结果                 |
| -d   | 选用的统计文件，默认为"pretrained_data" | 选定语料库（请先运行 -gf 或 -gfb） |
| -c   | 无                                      | 对比输出文件                       |
| -if  | 文件名，默认为"../data/input.txt"       | 指定输入文件的位置                 |
| -of  | 文件名，默认为"../data/output.txt"      | 指定输出文件的位置                 |
| -sf  | 文件名，默认为"../data/std_output.txt"  | 指定对比文件的位置                 |

其中：

1. `-r` 指令的参数可以选择 normal_2.py, normal_3.py, normal_23.py, smooth_2.py, smooth_3.py
2. `-d` 指令的参数可以选择 pretrained_data 和 pretrained_data_with_wikipedia
3. `-if`, `-of`, `-sf` 是以当前目录（src）下的对应位置，例如："../data/input.txt"

**请注意：由于文件大小限制，可以先在 https://github.com/brightmart/nlp_chinese_corpus 下载维基百科语料库，解压缩后放入`raw_data/corpus/wiki_zh` 内。（否则执行命令 `-gfb` 会出错）**

**接着可以运行：**

```
python3 main.py -gc -gf
```

若你已下载维基语料库且放入指定位置后，也可以运行：

```
python3 main.py -gfb
```

生成基础语料的统计文件。

**然后可以尝试下面的代码开始预测拼音：**

```
python3 main.py -r normal_2.py
python3 main.py -d pretrained_data_with_wikipedia -r normal_23.py
python3 main.py -d pretrained_data_with_wikipedia -r smooth_23.py
```

其中：

1. 第一行是使用新浪语料库的字二元模型；
2. 第二行是使用新浪语料库与维基语料库的字二、三元模型。
3. 第三行是使用新浪语料库与维基语料库的字二、三元平滑模型。

除此之外也可以使用其他命令组合测试喔！

