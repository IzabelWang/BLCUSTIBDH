# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 18:31:04 2018

@author: 可欣
"""
'''安装python-docx：

pip install python_docx'''
import docx
from docx import Document
path = "D:/GOT/dragon.docx"
document = Document(path)
for paragraph in document.paragraphs:
    print(paragraph.text)
'''运行后可以在结果视窗里看到文本内容'''