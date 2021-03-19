# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/18 11:31
# FileName : day12.2
# Description : 观察者模式
# --------------------------------

class Event(object):
    _observers = []

    def __init__(self,subject):
        self.subject = subject

    @classmethod
    def register(cls,observer):
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def unregister(cls,observer):
        if observer in cls._observers:
            cls._observers.remove(observer)

    @classmethod
    def notify(cls,subject):
        event = cls(subject)
        for observer in cls._observers:
            if isinstance(observer,str):
                print("string")
                return
            observer(event)

class WriteEvent(Event):
    # def __repr__(self):
    #     return 'WriteEvent'

    def __str__(self):
        return self.__class__.__name__

def log(event):
    print("%s was written" % event.subject)

WriteEvent.register(log)

# 2222
class AnotherObserver(object):
    def __call__(self, event):
        print('Yes %s '% event)

    def __str__(self):
        return "xx"

    def __new__(cls, event):
        print('Yes %s '% event)
        return super(AnotherObserver,cls).__new__(cls)

WriteEvent.register(AnotherObserver("log"))
WriteEvent.notify('a given file')

# tester
# WriteEvent.register('tester')
# WriteEvent.notify('tester')