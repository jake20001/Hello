# coding: utf-8
"""
    @author: zhangjk
    @file: 14.py
    @date: 2020-02-28
    说明：tuple
"""

def f1():
    tuple = ( 'python', 786 , 2.23, 'java', 70.2)
    tinytuple = (123, 'python')

    print (tuple)             # 输出完整元组
    print (tuple[0])          # 输出元组的第一个元素
    print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
    print (tuple[2:])         # 输出从第三个元素开始的所有元素
    print (tinytuple * 2)     # 输出两次元组
    print (tuple + tinytuple) # 连接元组


def f2():
    tinytuple = (123, 5)
    print(id(tinytuple))
    # tinytuple[1] = 'C'
    print(tinytuple[0])
    tup1 = ()    # 空元组
    tup2 = (20,) # 一个元素，需要在元素后添加逗号
    print(tup2)



def main():
    # f1()
    f2()


if __name__ == '__main__':
    main()