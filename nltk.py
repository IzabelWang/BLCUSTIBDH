# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:53:48 2018

@author: 可欣
"""

#Tokenizing text into sentences

para = "Hello World. It's good to see you. Thanks for buying this book."
from nltk.tokenize import sent_tokenize
sent_tokenize(para) 
# "sent_tokenize"是一个函数，下文很多中间带下划线的标识符都指的是函数。


#Tokenizing sentences into words
from nltk.tokenize import word_tokenize
word_tokenize('Hello World.')

# 等同于

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
tokenizer.tokenize('Hello World.')

# 等同于
import nltk
text = "Hello. Isn't this fun?"
pattern = r"\w+|[^\w\s]+" # r：regular expression；双引号""可以用单引号''代替；\w表示单词字符，等同于字符集合[a-zA-Z0-9_]；+表示一次或者多次，等同于{1,}，即c+ 和 c{1,} 是一个意思；"|"：二选一，正则表达式中的"或"； [...]：字符集（字符类），其对应的位置可以是字符集中任意字符，例如，a[bcd]表abe、ace和ade；^表示只匹配字符串的开头；\s匹配单个空格，等同于[\f\n\r\t\v]。
print(nltk.tokenize.regexp_tokenize(text, pattern))


import nltk
text = "Hello. Isn't this fun?"
pattern = r"\w+|[^\w\s]+" # r：regular expression；双引号""可以用单引号''代替；\w表示单词字符，等同于字符集合[a-zA-Z0-9_]；+表示一次或者多次，等同于{1,}，即c+ 和 c{1,} 是一个意思；"|"：二选一，正则表达式中的"或"； [...]：字符集（字符类），其对应的位置可以是字符集中任意字符，例如，a[bcd]表abe、ace和ade；^表示只匹配字符串的开头；\s匹配单个空格，等同于[\f\n\r\t\v]。
print(nltk.tokenize.regexp_tokenize(text, pattern))