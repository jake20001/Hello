# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/6/23 20:32
# FileName : 2
# Description : 
# --------------------------------


def gys(a,b):
    if a < b:
        b,a = a,b
    while a%b!=0:
        a,b = b,a%b
    print(b)


ages = [5, 16, 19, 22, 26, 39, 45]

def myFunc(x):
    print('x..',x)
    if x < 18:
        return False
    else:
        return True

def f2():
    adults = filter(myFunc, ages)

    for x in adults:
        print(x)


def Power(x,n):
    d = 1
    for i in range(n):
        d = d*x
    return d

def main():
    # gys(12,15)
    # f2()
    print(Power(2,3))

if __name__ == '__main__':
    main()