# -*- coding: utf-8 -*-

from gensim.models import word2vec

if __name__ == '__main__':
    model = word2vec.Word2Vec.load("zhwiki.model")

    # similarity of 2 words
    y1 = model.similarity("男人", "女人")
    print(u"男人和女人的相似度為：", y1)
    print("--------")

    # top n similarity, ex: n=20
    y2 = model.most_similar("同意", topn=20)
    print(u"和'同意'最相關的詞有：\n")
    for item in y2:
        print(item[0], item[1])
    print("--------")

    # the relationship
    print(' "男孩" 之於 "爸爸" 如 "女孩" 之於 ...? \n')
    y3 = model.most_similar(['男孩', '爸爸'], ['女孩'], topn=3)
    for item in y3:
        print(item[0], item[1])
    print("--------")
    
    # Which word from the given list doesn’t go with the others?
    y4 = model.doesnt_match("早餐 午餐 晚餐 大便".split())
    print(u"不合群的詞：", y4)
    print("--------")

