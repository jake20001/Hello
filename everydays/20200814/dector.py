# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : newTrains
# Author : zhangjk
# CreateTime : 2020/8/14 10:27
# FileName : dector
# Description : 
# --------------------------------


def using_logger(func):

    def wrapper(*args,**kwargs):
        print(u"%s 装饰器 ..." % func.__name__)
        return func(*args)
    return wrapper

@using_logger
def bar():
    print("i am bar")
    return "OK"

def main():
    bar()

if __name__ == '__main__':
    main()