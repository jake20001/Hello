# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/9/14 19:55
# FileName : s1
# Description : 
# --------------------------------
# from collections import Iterator, Collection, Sequence


class Demo(object):

    def __init__(self):
        self.ax = ['a','b','a']

    # def __getitem__(self):
    #     Sequence.__getitem__(1)
    #
    # def __contains__(self, item):
    #     Sequence.__contains__(item)
    #
    # def __iter__(self):
    #     Sequence.__iter__(self)
    #
    # def __len__(self):
    #     Sequence.__len__()

    def testsum(self,value):
        print(self)
        return len([1 for v in self.ax if v is value or v == value])

    def tesxx(self):
        # dc = {'a':1,'b':2,'c':3}
        # c = '1'
        dc = {1:'c',2:'b',3:'a'}
        print(sorted(dc.items(),key=lambda x:x[1]))
        return sum(dc)
        # for k,v in dc.items():
        #     print(k)

def main():
    mDemo = Demo()
    # print(mDemo.testsum('a'))
    print(mDemo.tesxx())

if __name__ == '__main__':
    main()