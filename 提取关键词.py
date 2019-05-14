# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 19:21:49 2018

@author: 可欣
"""
'''用jieba提取文本的关键词，每个语料提取前十个'''
from os import path
import jieba.analyse as analyse

d = path.dirname(__file__)

text_path = 'D:/GOT/corpara/1.txt' #设置要分析的文本路径
text = open(path.join(d, text_path)).read()

for key in analyse.extract_tags(text,10, withWeight=False):
# 使用jieba.analyse.extract_tags()参数提取关键字,默认参数为50
    print(key)

