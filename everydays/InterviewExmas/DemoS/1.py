# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/7/30 18:02
# FileName : 1
# Description : 
# --------------------------------

def fn(n):
    if n==0 or n==1:
        return 1
    return fn(n-1) + fn(n-2)

def fx(n):
    a = 1
    b = 1
    if n==1 or n==0:
        return 1
    for i in range(n-1):
        a ,b = b ,a+b
    return b


def main():
    print(fn(2))
    print(fn(3))
    print(fx(2))
    print(fx(3))

if __name__ == '__main__':
    main()
