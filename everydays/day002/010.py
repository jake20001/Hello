# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 15:23
# FileName : 010
# Description : 
# --------------------------------

class Foo(object):
    pass


foo = type('Foo',(),{})


def main():
    # F = Foo()
    # print(Foo,F)
    # F.a = 10
    # print(id(F.a))
    # f = foo()
    # print(foo,f)
    # print(f.a)

    print(Foo())
    print(foo())


if __name__ == '__main__':
    main()

class Foo(object):
    bar = True

    def __init__(self):
        self.name = 'name'

    # def echo_bar(self):
    #     print(self.bar)

class Aoo(Foo):
    pass

foo = type('Foo',(),{'bar':False})

boo = type('boo',(Foo,),{})

def echo_bar(self):
    print(self.bar)

coo = type('boo',(Foo,),{'echo_bar':echo_bar})


def main():
    # print(Foo())
    # print(foo())
    # print(Foo().bar,id(Foo().bar))
    # print(foo().bar,id(foo().bar))
    print(boo)
    print(boo.bar)
    print(boo().name,boo().bar)

    print(hasattr(Foo,'echo_bar'))
    print(hasattr(coo,'echo_bar'))

    coo().echo_bar()
