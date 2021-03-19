# coding: utf-8
"""
    @author: zhangjk
    @file: 14.py
    @date: 2020-02-28
    说明：iter  迭代器
"""

import sys         # 引入 sys 模块

def f1():
    # list=[1,2,3,4]
    list = "hello world"
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


# NEW
i = 0
a = 65
def func():
    global i

    i += 1
    return chr(a+i)

def iter2():
    # nstr = "Hello Python"
    # s = iter(nstr)
    # print('xxxx',s)
    # # for i in s:
    # #     print(i)
    # while True:
    #     try:
    #         print(next(s))
    #     except:
    #         break
    for i in iter(func,'P'):
        print(i)

def iter3():
    nstr = "Hello Python"

    next()


class data:
    list: list = [1, 2, 3, 4, 5, 6]
    index = 0

    def __call__(self, *args, **kwargs):
        item = self.list[self.index]
        self.index += 1
        return item

    def __iter__(self):
        self.i = iter(self.list)
        return self.i


# for item in iter(data(), 3):  #每一次迭代都会调用一次__call__方法,当__call__的返回值等于3是停止迭代
#     print(item)




def main():
    f1()

    # myclass = MyNumbers()
    # myiter = iter(myclass)
    # print(next(myiter))
    # print(next(myiter))
    # print(next(myiter))
    # print(next(myiter))
    # print(next(myiter))

    # iter2()
    # pass

if __name__ == '__main__':
    main()