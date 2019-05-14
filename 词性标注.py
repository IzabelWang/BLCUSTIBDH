# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 18:19:46 2018

@author: 可欣
"""
import jieba
import jieba.posseg as pseg

from os import path
import jieba.analyse as analyse

d = path.dirname(__file__)

text_path = 'D:/GOT/dragon.txt' #设置要分析的文本路径
text = open(path.join(d, text_path)).read()

result = pseg.cut(text)                     ##词性标注，标注句子分词后每个词的词性
for item in result:
    print(item)
print("【词性标注】------------------】")