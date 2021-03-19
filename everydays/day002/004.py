# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 14:12
# FileName : 004
# Description : 
# --------------------------------

class AA(type):

    @classmethod
    def __str__(cls):
        print("cls __str__")
        return super(AA,cls).__dict__.items().__str__()

    def __call__(self):
        print("self __call__")
        return super(AA,self).__call__()

    @staticmethod
    def goo():
        print("goo...")


    def __new__(cls, clsname, bases, attrs):
        print("cls __new__")
        return super(AA,cls).__new__(cls,clsname, bases, attrs)

    # def __new__(self, clsname, bases, attrs):
    #     print("self __new__")
    #     return super(AA,self).__new__(self,clsname, bases, attrs)

    @classmethod
    def __init__(cls, clsname, bases, attrs):
        print("cls __init__")
        return super(AA,cls).__init__(cls,clsname, bases, attrs)

    # def __init__(self,clsname, bases, attrs):
    #     print("self __init__")
    #     return super(AA,self).__init__(clsname, bases, attrs)

    @classmethod
    def coming(cls):
        print("coming")


def main():
    aa = AA('clsname', (object,), {'attrs':1})
    print(aa().__getattribute__('attrs'))
    aa.coming()
    # AA.goo()
    AA.coming()


if __name__ == '__main__':
    main()