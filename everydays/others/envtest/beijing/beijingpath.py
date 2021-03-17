# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/5 11:11
# FileName : shenzhoupath
# Description : 
# --------------------------------
import os

crpath = os.getcwd()
crpath = os.path.join(crpath,'../')
testpac = os.path.join(crpath, 'testpac')

def get_path():
    if os.path.exists(testpac):
        print("beijing...ok")
