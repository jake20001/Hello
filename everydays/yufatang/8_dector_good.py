# coding: utf-8
"""
    @author: zhangjk
    @file: 8_dector_good.py
    @date: 2020-02-28
    说明：xxxx
"""
from datetime import datetime


def jk():
    print('jk speaking')

##############################
# def jk2():
#     print('jk2 speaking')
#     date = datetime.utcnow()
#     print(date)


#### tom()、john()、Mary()也要输出类似句子。怎么做？ #####

# def date(func):
#     func()
#     date = datetime.utcnow()
#     print(date)
#
# def alan():
#     print('alan speaking')
#
# def tom():
#     print('tom speaking')

### 我们每次都要将一个函数传递写入date中，如果我要实现直接调用alan()或者tom()就可以输出结果，又要避免重复写相同的代码，应该怎么修改？###
def date(func):
    def wrapper():
        func()
        date = datetime.utcnow()
        print(date)
    return wrapper

def alan():
    print('alan speaking')

def tom():
    print('tom speaking')

################   装饰器  ########################
@date
def alan():
    print('alan speaking')

@date
def tom():
    print('tom speaking')

# 如果我们有其他的类似函数，我们可以继续调用decorator来修饰函数，而不用重复修改函数或者增加新的封装。这样，我们就提高了程序的可重复利用性，并增加了程序的可读性。

def main():
    # jk2()

    # date(jk)
    # date(tom)

    # t = date(tom)
    # t()
    # j = date(jk)
    # j()

    tom()
    alan()






if __name__ == '__main__':
    main()