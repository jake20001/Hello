# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 17:42
# FileName : 011
# Description : 
# --------------------------------

from __future__ import unicode_literals
import json

new_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['弄好', 800], ['shirt', 300]]}]}

def f1():
    with open("record.json","wb") as f:
        json.dump(new_dict,f,ensure_ascii=False)
        print("加载入文件完成...")

def f2():
    with open("anjuke_salehouse.json","w",encoding='utf-8') as f:
        json.dump(new_dict,f,ensure_ascii=False,sort_keys=True, indent=4)
    print(u'加载入文件完成...');
