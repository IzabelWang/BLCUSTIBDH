# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 18:01:23 2018

@author: 可欣
"""

from nltk.corpus import PlaintextCorpusReader
from nltk import word_tokenize
from nltk import Text
from nltk import FreqDist

corpus_root = ''
files = PlaintextCorpusReader(corpus_root,'.*\.txt')
files.fileids()
words = word_tokenize(files.raw(fileids=files.fileids()))
cps1 = Text(words)

fdist1 = FreqDist(cps1)
wl = fdist1.items()
wl_sorted_desc = sorted(wl, key=lambda w:w[1], reverse=True)
wl_sorted_asc = sorted(wl, key=lambda w:w[1])