# coding: utf-8
"""
    @author: zhangjk
    @file: 2.py
    @date: 2020-02-29
    说明：class
"""
# 几亿年前
import sys


class Animal(object):

    head = "HEAD"

    def __init__(self):
        self.name = 'animal'

    def bark(self):
        print('But person can talk')

    def sleep(self):
        print(self.name + ' must sleep, or maybe die')

# 1亿年前
class Fish(object):

    def __init__(self):
        self.name = 'fish'

    def breath(self):
        print(self.name + ' is ' + sys._getframe().f_code.co_name + ' with mouse ' + str(sys._getframe().f_code.co_stacksize))

    def swimming(self):
        print(self.name + ' is ' + self.__class__.__name__ + ' and ' + sys._getframe().f_code.co_name)

# 几千年前
class Wolf(object):

    def __init__(self):
        self.name = 'wolf'

    def bark(self):
        print(self.name + " is barking " + self.__class__.__name__)


class Dog(Wolf,Fish,Animal):

    # 私有变量
    __my_dog = '小聪明'

    def __init__(self):
        Wolf.__init__(self)
        Fish.__init__(self)
        Animal.__init__(self)
        # self.name = "WangWang"
        # self.type = 'DeMu'

    # def breath(self):
    #     self.name = "Huahua"
    #     print(self.name + ' is ' + sys._getframe().f_code.co_name + ' with mouse ' + str(sys._getframe().f_code.co_stacksize))

    def bark(self):
        print(self)
        print(self.__class__)
        print(self.name + " is barking wangwang ....")

    def housekeeping(self):
        print(self.name + ' can house keeping')

    def just_me_call(self):
        print(Dog.__my_dog  + ' is my called')

    # 私有方法
    def __just_private_for_me(self):
        return (Dog.__my_dog + ' , i try think your mind')

    def visit_private_name(self):
        print(self.__just_private_for_me())


def main():
    mDog = Dog()

    # mDog.swimming()

    # mDog.housekeeping()
    # mDog.sleep()
    # mDog.breath()

    # super(Dog,mDog).bark()
    # d.__thisclass__().bark()
    mDog.bark()


    # 怎么知道子类是调用了那个父类的方法；指明
    # d = super(Animal,Animal)
    # d.__thisclass__().bark()


    # print(Dog.head)

    # print(Dog.__my_dog)
    # mDog.just_me_call()

    # mDog.__just_private_for_me()
    # mDog.visit_private_name()




if __name__ == '__main__':
    main()
