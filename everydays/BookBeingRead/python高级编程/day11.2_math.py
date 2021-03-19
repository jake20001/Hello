# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/18 15:07
# FileName : day11.2_math
# Description : 
# --------------------------------

def how_many_times(son,dad,n):
    while(dad<100):
        if (dad==n*son):
            print('son',son)
        dad = dad+1
        son = son+1

how_many_times(4,40,4)

