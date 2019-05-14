# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 19:11:13 2018

@author: 可欣
"""

import time
import win32com.client as win32
 
#----------------------------------------------------------------------
def excel():
    """"""
    xl = win32.gencache.EnsureDispatch('Excel.Application')
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
 
    xl.Visible = True
    time.sleep(1)
 
    sh.Cells(1,1).Value = 'Hacking Excel with Python Demo'
 
    time.sleep(1)
    for i in range(2,8):
        sh.Cells(i,1).Value = 'Line %i' % i
        time.sleep(1)
 
    ss.Close(False)
    xl.Application.Quit()
 
if __name__ == "__main__":
    excel()
    
'''运行后会有excel自动打开，按时间递增行数'''
