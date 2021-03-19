# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/11/26 15:25
# FileName : day1.2
# Description : 迭代器和生成器
# --------------------------------
import pandas

# 迭代器
def f1(ax):
    l=iter(ax)
    # print(l)
    # print(list(l))
    # print(next(l))
    # print(next(l))
    # print(next(l))
    # print(next(l))
    for i in l:
        print(i)

# f1('abc')
# f1(['abc'])
# f1(['aa','bb','cc'])

# 写一个迭代器:输出一组list
class MyIterator(object):

    def __iter__(self):
        return self

    # def __init__(self,seq):
    #     self.seq = seq
    #     self.steps = len(seq)

    # 堆
    # def __next__(self):
    #     if self.steps==0:
    #         raise
    #     self.steps = self.steps -1
    #     return self.seq[self.steps]

    def __init__(self,seq):
        self.seq = seq
        self.steps = -1

    # 队列
    def __next__(self):
        if self.steps+1==len(self.seq):
            raise StopIteration
        self.steps = self.steps+1
        return self.seq[self.steps]

# mMyIterator = MyIterator(['a','b','c'])
# print(mMyIterator)
# print(next(mMyIterator))
#
# for el in mMyIterator:
#     print(el)


# yield: 生成器
def fabi():

    a ,b = 0,1
    while True:
        yield a
        a,b = b,a+b

# f = fabi()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# # for i in range(10):
# #     print(next(f))
# print([next(f) for i in range(10)])

# 生成器 send ： next
def pyschologist():
    print("please tell me something")
    try:
        while True:
            answer = yield
            if answer is not None:
                if answer.endswith('?'):
                    print("111111111")
                    break
                elif 'good' in answer:
                    print("222222222222")
                elif 'bad' in answer:
                    print("33333333333")
            print("xxxxxxxx")
        print("yyyyyyy",1/0)
    except ValueError:
        yield 'error 44444444'
    finally:
        print('ok close')


free = pyschologist()
print(free)
line = next(free)
# print(line)
while True:
    try:
        answer = input()
        free.send(answer)
    except:
        free.throw(ValueError('mean'))
        free.close()
        break




