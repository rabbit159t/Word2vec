# Word2Vec

## Usage
```
1.download wiki data
https://dumps.wikimedia.org/zhwiki/latest/
https://dumps.wikimedia.org/enwiki/latest/
don't decompress the bz2 file now

2.python wiki_to_txt.py wiki.xxx.xml.bz2
transfer wiki.xml to wiki.txt

3.python wiki_preprocess.py
simplified to traditional
use jieba to cut word

4.python train.py


## Environment
Python 3.6.3</br>
Windows 7</br>
