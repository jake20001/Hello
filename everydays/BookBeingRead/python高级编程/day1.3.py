# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/11/26 20:16
# FileName : day1.3
# Description : 
# --------------------------------
import multitask

import time

def coroutine_1():
    for i in range(3):
        print('c1')
        yield i

def coroutine_2():
    for i in range(3):
        print('c2')
        yield i

multitask.add(coroutine_1())
multitask.add(coroutine_2())
multitask.run()








