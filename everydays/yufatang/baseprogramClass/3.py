# coding: utf-8
"""
    @author: zhangjk
    @file: 3.py
    @date: 2020-02-29
    说明：类的专有方法
"""
import operator


class Dog(object):

    def __init__(self,name,num):
        self.name = name
        self.num = num

    def __call__(self, *args, **kwargs):
        pass

    def __add__(self, other):
        return self.num + other.num

    # def __cmp__(self, other):
    #     if self.name < other.name:
    #         return -1
    #     elif self.name > other.name:
    #         return 1
    #     return 0

    def __eq__(self, other):
        print("重写了__eq__")
        if self.name==other.name:
            return True
        return False

    # def __eq__(self, other):
    #     print("重写了__eq__")
    #     if isinstance(other, self.__class__):
    #         return self.__dict__ == other.__dict__
    #     else:
    #         return False

    def __str__(self):
        return "my name is " + self.name

    def __hash__(self):
        print(self.name + '使用了hash函数',hash(self.name))
        return hash(self.name)


def main():
    mDog1 = Dog('Wang',1)
    print(mDog1)
    mDog2 = Dog('Wang',2)
    print(mDog2)
    print(mDog2 + mDog1)
    print(mDog1==mDog2)
    # mDogs = set([mDog1,mDog2])
    # mDog3 = Dog('Worf',3)
    # print(mDog3)
    # mDogs.add(mDog3)
    # print(mDogs)
    # mDogs.add(mDog3)
    # print(mDogs)


if __name__ == '__main__':
    main()