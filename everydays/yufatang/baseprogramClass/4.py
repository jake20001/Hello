# coding: utf-8
"""
    @author: zhangjk
    @file: 4.py
    @date: 2020-02-29
    说明：作用域
"""


# var1 是全局名称
var1 = 5
def some_func():
    global var1

    # 想要改变var1
    var1 = 50
    # var2 是局部名称
    var2 = 6
    print(var2)
    def some_inner_func():
        # 改变闭包变量
        nonlocal var2

        # var3 是内嵌的局部名称
        var3 = 7
        var2 = 100
        print('some_inner_func',var2)
        return var3
    print('some_func',var2)
    return some_inner_func


def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
    print('no nonlocal',num)
    inner()
    print('nonlocal',num)


def main():
    # print(var1)
    # s = some_func()
    # print(s())
    # print(var1)
    # print()

    outer()




if __name__ == '__main__':
    main()