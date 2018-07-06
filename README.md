# Word2Vec
## Usage
1. Download wiki data
[zhwiki](https://dumps.wikimedia.org/zhwiki/latest/) or [enwiki](https://dumps.wikimedia.org/enwiki/latest/)
Don't decompress .bz2 now

2. ```$python wiki_to_txt.py wiki.xxx.xml.bz2```
(transfer wiki.xml to wiki.txt)

3. ```$python processing_zh.py``` (for Chinese)
[1.] simplified to traditional
[2.] use jieba to cut word and segment the text
[dict.txt.big](https://github.com/fxsjy/jieba/blob/master/extra_dict/dict.txt.big)

4.  ```$python train.py```
(train the wiki model)
5. ```$python demozh.py```


## Environment
Python 3.6.3</br>
Windows 7</br>
