# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/7/30 18:26
# FileName : 3
# Description : 
# --------------------------------
import math


def dengbi(a,n):
    s = 1
    for i in range(1,n):
        s = s + math.pow(a,i)
    return s

def p(a,n):
    return math.pow(a,n)


def main():
    print(dengbi(2,3))
    print(p(2,3))


if __name__ == '__main__':
    main()
