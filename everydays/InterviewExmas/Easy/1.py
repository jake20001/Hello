# -*- coding:utf-8 -*-
# -------------------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/4/27 9:56
# FileName : 1
# Description :   1, s = 1 + 2 ...+ n
#                 2, s = n!
#                 3, F(n) = F(n-1) + F(n-2)
#                 4, s = 2^n
#                 5, lambda
#                 6,为什么字符串是不能改变的
# -------------------------------------------
import math

# ============== SUM BEGIN ==================
def Sum1(n):
    s = 0
    for i in range(n):
        s = s + i
    return s

def Sum2(n):
    return sum(i for i in range(n))

def Sum(n):
    y = 0
    for i in range(n):
        f = Fx(i)
        y = y + next(f)
    return y

def Fx(x):
    yield x
# ============== SUM END ====================

# ============== 阶层 Rank BEGIN ============
def Rank(n):
    if n==0:
        return 1
    return n*Rank(n-1)
# ========== 阶层 Rank END ==================

# ============ 斐波那契级数 BEGIN ============
def Firb(n):
    if n==0 or n==1:
        return 1
    return Firb(n-1) + Firb(n-2)
# ==========  斐波那契级数 END ===============

# =========== 指数 BEGIN ====================
def Power1(x,n):
    return x**n

def Power2(x,n):
    return math.pow(x,n)

def Power(x,n):
    d = 1
    for i in range(n):
        d = d*x
    return d
# ============= 指数 END ====================

# ============ lambda BEGIN==================
def fun2(dt):
    return dt[1]

def LamdbaUnderstand():
    dict1 = {'a':2,'b':1}
    print(sorted(dict1.items(),key=lambda item: item[1]))
    print(sorted(dict1.items(),key=fun2))
# ============= lambda END =================

# ========= 证明字符串不能改变 BEGIN===========
def Address():
    s1 = "Python"
    add1 = id(s1)
    print(s1,add1)
    s1 = s1 + " Hello"
    add2 = id(s1)
    print(s1,add2)
    print(add1==add2)
# ============ 证明字符串不能改变 END ===========


def main():
    # print(Sum(101))
    # print(Rank(3))
    # print(Firb(5))
    # print(Power(2,3))
    LamdbaUnderstand()


if __name__ == '__main__':
    main()