# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : newTrains
# Author : zhangjk
# CreateTime : 2020/8/13 15:58
# FileName : newinit
# Description : 
# --------------------------------

class A(object):

    def __new__(cls, *args, **kwargs):
        print("A.__new__ is called")
        # return object.__new__(cls)
        # return Sample()
        mcls = super(A,cls).__new__(cls)
        print('mcls',mcls,id(mcls))
        return mcls
        # return Sample.__new__(cls)
        # return object.__new__(cls)

    def __init__(self):
        # super(A,self).__init__()
        print('self',self,id(self))
        print("A.__init__ is called")

    def __str__(self):
        return "HAHA"



class Sample(object):

    def __str__(self):
        return "SAMPLE"




def main():
    a = A()
    print(a)


if __name__ == '__main__':
    main()