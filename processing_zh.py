# -*- coding: utf-8 -*-
import jieba
import logging
from opencc import OpenCC

if __name__ == "__main__":
    print("-----开放中文转换-----")
    openCC = OpenCC('s2t')  # https://github.com/yichen0831/opencc-python
    with open("zhwiki_tmp.txt", "r", encoding="utf-8") as simplified:
        with open("zhwiki.txt", 'w', encoding='utf-8') as output:
            for s in simplified:
                converted = openCC.convert(s)
                output.write(converted)

    jieba.set_dictionary('.\\data\\dict.txt.big')
    jieba.load_userdict('.\\data\\userdict.txt')
    # load stopwords set
    stopword_set = set()
    with open('.\\data\\stopwords.txt', 'r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))

    with open('zhwiki.txt', 'r', encoding='utf-8') as content:
        with open("zhwiki_seg.txt", 'w', encoding='utf-8') as output:
            for i, line in enumerate(content):
                line = line.strip('\n')
                words = jieba.cut(line, cut_all=False)
                for word in words:
                    if word not in stopword_set:
                        output.write(word + ' ')
                output.write('\n')
                # if i == 5:
                # break

                if (i + 1) % 10000 == 0:
                    logging.info("finished " + str(i + 1))
