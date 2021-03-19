# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/4/27 14:09
# FileName : 1
# Description : 1, 如何理解yield程序，print结果上什么？
# --------------------------------

# =========== Yield BEGIN ===============
def add(n, i):
    return n+i

def test():
    for i in range(4):
        yield i

def quickAdd():
    g = test()
    for n in [1, 10, 5]:
        g = (add(n, i) for i in g)
    print(list(g))
# =========== Yield END =================

def main():
    quickAdd()

if __name__ == '__main__':
    main()