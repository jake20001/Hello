# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/4 14:15
# FileName : day1
# Description :
# f(n)=f(n-1)+f(n-2)
# --------------------------------

def f1(n):
    if n==0 or n==1:
        return 1
    return f1(n-1)+f1(n-2)

def f2(n):
    a = 1
    b = 1
    if n==1 or n==0:
        return 1
    for i in range(n-1):
        a,b = b ,a+b
    return b

mt = {1:f1,2:f2}

if __name__ == '__main__':
    f = mt[2]
    print(f(0))
    print(f(3))