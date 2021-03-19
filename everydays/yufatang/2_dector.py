# coding: utf-8
"""
    @author: zhangjk
    @file: 2_dector.py
    @date: 2020-02-28
    说明：xxxx
"""

# 装饰器说明
# Python中的装饰器是一种可以装饰其它对象的工具。
# 该工具本质上是一个可调用的对象（callable），所以装饰器一般可以由函数、类来实现。
# 装饰器本身需要接受一个被装饰的对象作为参数，该参数通常为函数、方法、类等对象。
# 装饰器需要返回一个对象，该对象可以是 经过处理的原参数对象、一个包装且类似原参数的对象；或者返回一个不相干内容（通常不建议使用）


def warp(obj):
    return obj

@warp
def foo():
    print('hello decorator!')





def main():
    # 1
    # print(warp('hello decorator!'))
    # 2
    # f = warp(foo)
    # f()
    # 3
    # @warp    # 等价于 foo = warp(foo)
    # def foo2():
    #     print('hello decorator!')
    foo()    # => hello decorator!



if __name__ == '__main__':
    main()