# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/18 10:19
# FileName : day11.1_math
# Description :
# n=0,1,2,3,4,5      s =1,2,4,7,11,16
# --------------------------------

def how_many_cut(n):
    d = 1
    s = 1
    for i in range(n):
        s = s + d
        d = d + 1
    return s

if __name__ == '__main__':
    for i in range(6):
        print(how_many_cut(i))
