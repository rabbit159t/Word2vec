# Word2Vec
## Usage
1. Download wiki data
[zhwiki](https://dumps.wikimedia.org/zhwiki/latest/) or [enwiki](https://dumps.wikimedia.org/enwiki/latest/)</br>
Don't decompress .bz2 now

2. Transfer wiki.xml to wiki.txt
    ```
    $python wiki_to_txt.py wiki.xxx.xml.bz2
    ```

3. Simplified to traditional & segment the text (for Chinese)
    ```
    $python processing_zh.py
    ```
4.  Train the wiki model
    ```
    $python train.py
    ```
5. Show the result
    ```
    $python demozh.py
    ```


## Environment
Python 3.6.3</br>
Windows 7</br>

## Resource
[dict.txt.big](https://github.com/fxsjy/jieba/blob/master/extra_dict/dict.txt.big)
