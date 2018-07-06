# -*- coding: utf-8 -*-

import logging
from gensim.models import word2vec

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # sg = 0, CBOW; sg = 1, Skip - gram
    model = word2vec.Word2Vec(word2vec.LineSentence("zhwiki_seg.txt"), size=250, workers=1,
                              window=5, min_count=10, sg=0)

    model.save("zhwiki.model")
