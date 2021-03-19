# coding: utf-8
"""
    @author: zhangjk
    @file: 5.py
    @date: 2020-02-28
    说明：生成器
"""

import sys

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

def f1():
    f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()

def save():
    for i in range(10):
        yield i

def output():
    s = save()
    while True:
        try:
            print(next(s))
        except:
            sys.exit()


def main():
    # f1()
    output()


if __name__ == '__main__':
    main()