#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys
from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    logging.info("running %s" % ' '.join(sys.argv))

    if len(sys.argv) != 3:
        print("Using: python wiki_to_txt.py zhwiki-latest-pages-articles.xml.bz2 zhwiki_tmp.txt")
        sys.exit(1)

    infile, outfile = sys.argv[1:3]
    wiki_corpus = WikiCorpus(infile, lemmatize=False, dictionary={})

    with open(outfile, 'w', encoding='utf-8') as output:
        i = 0
        for text in wiki_corpus.get_texts():
            output.write(' '.join(text) + '\n')
            i += 1
            if i % 10000 == 0:
                logging.info("Saved " + str(i) + " articles")
        print("Finished!")
