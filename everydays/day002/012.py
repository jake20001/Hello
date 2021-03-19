# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 17:50
# FileName : 012
# Description : 
# --------------------------------

class MetaClass(type):
    def __init__(cls, *args, **kwargs):
        # cls 代指以该类为元类的类 Foo
        print("MetaClass.__init__: ", cls)
        super(MetaClass, cls).__init__(*args, **kwargs)

    def __new__(mcs, *args, **kwargs):
        # mcs 代指元类自身
        print("MetaClass.__new__: ", mcs)
        return super().__new__(mcs, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        # cls 代指以该类为元类的类 Foo
        print("CLS: ", cls)
        # obj = cls.__new__(cls, *args, **kwargs)
        # cls.__init__(obj, *args, **kwargs)
        # return
        return super().__call__(cls, *args, **kwargs)


class Foo(metaclass=MetaClass):
    # 定义类Foo时，将调用元类的__new__方法和__init__方法。就跟一般普通类实例化时调用__new__方法和__init__方法一样。
    def __init__(self, name):
        self.name = name
        print("Foo.__init__: ", self)


# Foo 实例化时会调用元类的__call__方法。
a = Foo()


class Singleton(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

a = Singleton.instance(1,2)
b = Singleton.instance(2,3)
print(a.x)
print(b.x)
print(id(a)==id(b))

# lt(a, b) 相当于 a < b
# le(a,b) 相当于 a <= b
# eq(a,b) 相当于 a == b
# ne(a,b) 相当于 a != b
# gt(a,b) 相当于 a > b
# ge(a, b)相当于 a>= b
from operator import gt

def f1():
    di = {'>':gt}
    print(di['>'](2,1))

