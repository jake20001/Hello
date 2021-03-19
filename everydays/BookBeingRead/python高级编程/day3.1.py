# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/3 14:51
# FileName : day3.1
# Description : 
# --------------------------------

def mydecorator(function):
    def _mydecorator(*args,**kwargs):
        print("do something before")
        res = function(*args,**kwargs)
        print("do something after")
        return res
    return _mydecorator

def myprint():
    print("MMMMMMMM")
    return 'OK'

def mydecorator2(arg1,arg2):
    def _mydecorator(function):
        def __mydecorator(*args,**kwargs):
            print("Done before")
            res = function(arg1,arg2)
            print("Done after")
            return res
        return __mydecorator
    return _mydecorator

def myprint2(arg1,arg2):
    print("mmmmmm",arg1,arg2)
    return arg1,arg2

# Main
@mydecorator
def how_count():
    print("it is 1")

@mydecorator2(1,2)
def how_number(arg1,arg2):
    print('it is',arg1,arg2)


def main():
    # case = mydecorator(myprint)
    # print(case())

    # case = mydecorator2(1,2)
    # c = case(myprint2)
    # print(c())

    # how_count()

    how_number(3,4)


if __name__ == '__main__':
    main()