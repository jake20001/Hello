# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 13:36
# FileName : 002
# Description : 
# --------------------------------

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print(body)
        if not "bar" in body:
            raise TypeError("bar not implemented")
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

    def bar(self):
        return "bar"

class Derived(Base):
    def foo2(self):
        return "i am foo2"

m = Derived()
