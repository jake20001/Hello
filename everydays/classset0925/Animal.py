# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/9/18 17:42
# FileName : Animal
# Description : 
# --------------------------------
import sys


class Fish(object):

    def __init__(self):
        self.name = self.__class__.__name__.lower()

    def run(self):
        print(self.name + '\t' + sys._getframe().f_code.co_name + ' swimming ...')

class Crawler(object):

    def __init__(self):
        self.name = self.__class__.__name__.lower()

    def run(self):
        print(self.name + '\t' + sys._getframe().f_code.co_name + ' crawling...')


class Dog(object):

    def __init__(self):
        self.name = self.__class__.__name__.lower()

    def run(self):
        print(self.name + '\t' + sys._getframe().f_code.co_name + ' barking ...')


class Clild(Fish,Crawler,Dog):

    def __init__(self):
        self.name = self.__class__.__name__.lower()

    def run2(self):
        print(self.name + '\t' + sys._getframe().f_code.co_name)






def main():
    # mAnimal = Animal()
    # mAnimal.run()
    mClild = Clild()
    mClild.run()
    print(Clild.mro())


if __name__ == '__main__':
    main()