# coding: utf-8
"""
    @author: zhangjk
    @file: 2.py
    @date: 2020-02-28
    说明：数字 num
"""
import math


def f1():
    counter = 100          # 整型变量
    miles = 1000.0       # 浮点型变量
    name = "runoob"     # 字符串

    print(counter)
    print(miles)
    print(name)

class A():
    pass

class B(A):
    pass

def f2():
    print(isinstance(A(), A))
    print(type(A()) == A )
    print(isinstance(B(), A))
    print(type(B()) == A)

def f3():
    a, b, c, d = 20, 5.5, True, 4+3j
    print(type(a), type(b), type(c), type(d))


def f4():
    a = 1
    b = 2
    print(vars())
    print(locals())

def f5():
    a = 1
    print(a,id(a))
    del a
    print(a)
    print(id(a))

def f6():
    a = 5 + 4  # 加法
    print(a)
    b = 4.3 - 2 # 减法
    print(b)
    c = 3 * 7  # 乘法
    print(c)
    d = 2 / 4  # 除法，得到一个浮点数
    print(d)
    e = 2 // 4 # 除法，得到一个整数
    print(e)
    f = 17 % 3 # 取余
    print(f)
    g = 2 ** 5 # 乘方
    print(g)
    k = (1+1j)*(1-1j)
    print(k)
    x = complex(1+1j,1-1j)
    y = complex(1+1j).imag
    l = complex(1+1j)
    z = l.conjugate()
    m = l*z
    print(x)
    print(y)
    print(z)
    print(m)

def f7():
    a = 65
    b = bin(65)
    print(b)
    c = a >> 2
    print(c)

def f8():
    print(math.pi)
    print(math.e)
    print(math.log(2,2))


def main():
    # f2()
    # f3()
    # f4()
    # f5()
    # f6()
    f7()
    f8()


if __name__ == '__main__':
    main()