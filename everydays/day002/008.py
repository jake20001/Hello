# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 15:03
# FileName : 008
# Description : 
# --------------------------------
class Singleton(object):
    __instance = None

    def __new__(cls, age,*args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,age,*args, **kwargs):
        print("__init__",self)


def main():
    a = Singleton(18,"Dog")
    b = Singleton(8,"Chick")
    print(id(a))
    print(id(b))
    a.age = 20
    print(id(a))
    print(a.age)
    print(b.age)


if __name__ == '__main__':
    main()
