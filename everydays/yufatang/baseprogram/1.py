# coding: utf-8
"""
    @author: zhangjk
    @file: str2excel.py
    @date: 2020-02-28
    说明：斐波纳契数列
"""

def f1():
    # Fibonacci series: 斐波纳契数列
    # 两个元素的总和确定了下一个数
    a, b = 1, 1
    while b < 1000:
        print(b, end=',')
        a, b = b, a+b
        print(b/(a+b))


def fib_recur(n):
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    return fib_recur(n-1) + fib_recur(n-2)



def main():
    # f1()
    for i in range(1, 20):
        print(fib_recur(i), end=' ')
        print(fib_recur(i)/fib_recur(i+1))


if __name__ == '__main__':
    main()