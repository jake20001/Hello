# coding: utf-8
"""
    @author: zhangjk
    @file: 14.py
    @date: 2020-02-28
    说明：iter  迭代器
"""

import sys         # 引入 sys 模块

def f1():
    list=[1,2,3,4]
    it = iter(list)    # 创建迭代器对象

    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x




def main():
    # f1()

    myclass = MyNumbers()
    myiter = iter(myclass)
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))

if __name__ == '__main__':
    main()