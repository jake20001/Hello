# coding: utf-8
"""
    @author: zhangjk
    @file: 4_dector.py
    @date: 2020-02-28
    说明：xxxx
"""

# 用于模拟对象的装饰器--函数装饰器

def outer(func):         # 函数装饰器
    def inner():
        func()

    return inner


@outer      # foo = outer(foo)
def foo():
    print('hello foo')

print(foo)
print(foo.__name__)
foo()    # => hello foo