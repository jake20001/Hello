# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : newTrains
# Author : zhangjk
# CreateTime : 2020/8/12 15:13
# FileName : Fibr
# Description : 
# --------------------------------
def fibr(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibr(n-1) + fibr(n-2)

def fibr2(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b,a+b
    return a

# 黄金分割线 0.618
def goldLine(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b,a+b
    return a/b

def goldLine2(n):
    return fibr(n-1)/fibr(n)

# 验证相邻性
def distanceOne(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b,a+b
    x = a
    y = b
    z = a+b
    print(x*z,y**2)
    if abs(y**2-x*z)==1:
        return True
    return False


def main():
    # print(fibr(100))
    print(fibr2(100))
    print(goldLine(100))
    # print(goldLine2(50))
    print(distanceOne(3))

    for i in range(1, 20):
        print(fibr(i), end=' ')
        print(fibr(i)/fibr(i+1))


if __name__ == '__main__':
    main()