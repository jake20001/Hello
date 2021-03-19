# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : newTrains
# Author : zhangjk
# CreateTime : 2020/8/14 14:07
# FileName : 1
# Description : 
# --------------------------------



def fn1(n):
    y=1
    for i in range(1,n+1):
        y = i*y
    return y

def fuction(n):
    if (n>=1):
        result = n*fuction(n-1)
    elif (n==0):
        result = 1
    return result


def fn(n):
    if n==0:
        return 1
    return n*fn(n-1)

def main():
    print(fn(4))
    print(fuction(4))

if __name__ == '__main__':
    main()