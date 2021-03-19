# coding: utf-8
"""
    @author: zhangjk
    @file: 10.py
    @date: 2020-02-28
    说明：异常
"""
import sys


def f1():
    while True:
        try:
            x = int(input("请输入一个数字: "))
            break
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")

def runoob(a,b):
    return a/b


def f2(a,b):
    try:
        runoob(a,b)
    except AssertionError as error:
        print(error)
    else:
        try:
            with open('file.log') as file:
                read_data = file.read()
        except FileNotFoundError as fnf_error:
            print(fnf_error)
    finally:
        print('这句话，无论异常是否发生都会执行。')

def f3():
    assert (1)
    assert (1==1)
    # assert ('linux' in sys.platform)


# f1()
# f2(1,0)
# f2(1,2)
f3()