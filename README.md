# Word2Vec

## Usage
```
1.download wiki data
https://dumps.wikimedia.org/zhwiki/latest/
https://dumps.wikimedia.org/enwiki/latest/
Don't decompress .bz2 now

2.python wiki_to_txt.py wiki.xxx.xml.bz2
transfer wiki.xml to wiki.txt

3.python processing_zh.py (for Chinese)
simplified to traditional
use jieba to cut word
dict.txt.big: https://github.com/fxsjy/jieba/blob/master/extra_dict/dict.txt.big

4.python train.py


## Environment
Python 3.6.3</br>
Windows 7</br>
