# coding: utf-8
"""
    @author: zhangjk
    @file: 5.py
    @date: 2020-02-28
    说明：set
"""

def f1():
    student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
    print(student)   # 输出集合，重复的元素被自动去掉


    s = set(['Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'])
    print(s)

    s1 = set({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'})
    print(s1)

    # 成员测试
    if 'Rose' in student :
        print('Rose 在集合中')
    else :
        print('Rose 不在集合中')

    # set可以进行集合运算
    a = set('python')
    b = set('pyc')

    print(a)

    print(a - b)     # a 和 b 的差集

    print(a | b)     # a 和 b 的并集

    print(a & b)     # a 和 b 的交集

    print(a ^ b)     # a 和 b 中不同时存在的元素

    print((a | b) - (a & b))

def f2():
    s1 = set({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'})
    print(s1,id(s1))
    s1.add('Jane')
    print(s1,id(s1))
    s1.remove('Jack')
    print(s1,id(s1))
    s1.pop()
    print(s1,id(s1))
    # s1.update('Ann')
    # print(s1,id(s1))
    s1 = s1.union({'Ann'})
    print(s1,id(s1))
    s1 = s1.union('Ann')
    print(s1,id(s1))


def main():
    # f1()
    f2()

if __name__ == '__main__':
    main()