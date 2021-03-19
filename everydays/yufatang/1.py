# coding: utf-8
"""
    @author: zhangjk
    @file: str2excel.py
    @date: 2020-02-27
    说明：神奇的Python
"""
from functools import reduce


def theMAX():
    b = 2
    c = 3
    if b > c:
        a = b
    else:
        a = c
    return a

def theMAX2(b,c):
    a = max(b, c)
    print("1-->",a)
    a = c > b and c or b
    print("2-->",a)
    a = c if c > b else b
    print("3-->",a)

def theMAX3(b,c):
    a = [b, c][c > b]
    print("4-->",a)

def magic():
    a = 1; b = 2; c = 3
    b, c = c, b
    print(b,c)
    isBool = a < c < b < 5
    print(isBool)
    print('1' * 100)
    hb = [1,2,3,4] + [5,6,7,8]
    print(hb)

def magic2():
    l = [1, 2, 3, 4, 5]
    print(l[2])  # 3
    print(l[:3])  # 1,2,3
    print(l[3:])  # 4,5
    print(l[2:4])  # 3,4
    print(l[:-1])  # 1,2,3,4
    print(l[:])   #  1,2,3,4,5
    print(l[::2])  # 1,3,5

def ugly():
    for i in range(0):
        print(i)
        break
    else:
        print('for end')

def ugly2():
    i = 0
    while i:
        print(i)
        i -= 1
        break
    else:
        print('while end')

def ugly3():
    try:
        1 / 1
    except Exception as e:
        print('except occured')
    else:
        print('it is fine')
    finally:
        print('i am finally')

# 动态参数
def example_dynamic_args(*args, **kwargs):
    '''动态参数'''
    print(args)
    print(kwargs)

# 匿名函数
def anonymous_fuc(x):
    g = lambda x: x*2
    return g(x)

# 等价于
def equals_anonymous_fuc(x):
    return x*2

# filter, map, reduce
def magic3():
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
    f = filter(lambda x: x % 3 == 0,foo)
    print(list(f))
    m = map(lambda x: x * 2 + 10, foo)
    print(list(m))
    r = reduce(lambda x, y: x + y, foo)
    print(r)

def magic4():
    in_dict = {'a': 10, 'b': 2, 'c': 3}
    print('in_dict:', in_dict)
    out_dict = sorted(in_dict.items(), key=lambda x: x[1])
    print('out_dict', out_dict)
    print('out_dict', dict(out_dict))

# 列表推导表达式
def magic5():
    in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]
    print('array before:', in_list)
    array = [i for i in in_list if i % 2 != 0] # 列表推导表达式
    print('array after:', array)
    print('array after:', set(array))


# 生成器推导表达式
def magic6():
    in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]
    print('array before:', in_list)
    array = (i for i in in_list if i % 2 != 0)  # 生成器推导表达式
    print('array after:', array)
    print('array after:', list(array))

# 集合推导表达式
def magic7():
    in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]
    print('array before:', in_list)
    array = {i for i in in_list if i % 2 != 0} # 集合推导表达式
    print('array after:', array)

# 字典推导表达式
def magic8():
    in_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7]
    print('array before:', in_list)
    array = {i: i * 2 for i in in_list if i % 2 != 0}  # 字典推导表达式
    print('array after:', array)


# yield表达式
def example_generator(in_list):
    '''生成器'''
    for i in in_list:
        yield i

def example_generator2(in_list):
    '''生成器'''
    for i in in_list:
        res = yield i * 2
        # print(res)

def test_generator2():
    ep2 = example_generator2([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7])
    while True:
        print(next(ep2))


# yield的函数是一个生成器;yield相当于return后继续执行
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)

def foo_test1():
    g = foo()
    print(next(g))
    print("*"*20)
    print(next(g))

def foo_test2():
    g = foo()
    print(next(g))
    print("*"*20)
    print(g.send(7))

#### 为什么用这个生成器，是因为如果用List的话，会占用更大的空间 #####
def foo2(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num

def foo2_test3():
    for n in foo2(0):
        print(n)

# 闭包、生成器、装饰器,编写高并发程序时则要掌握协程相关知识
def example_decorator2(func):
    '''装饰器'''
    def inner():
        func()

    return inner

def example_decorator3(func):
    '''装饰器'''
    def inner():
        func()

    return inner()

def example_decorator(func):
    '''装饰器'''
    def inner():
        return func()

    return inner()

def func():
    print("Hello Python!")
    return 0



def main():
    # print(theMAX())
    # theMAX2(2,3)
    # theMAX3(2,3)
    # magic()
    # magic2()
    # ugly()
    # ugly2()
    # ugly3()
    # example_dynamic_args(1,'2', True, name='xiaowu', age=18)
    # example_dynamic_args([1,'2', True],1, name='xiaowu', age=18)
    # example_dynamic_args(1,'2', True, ['a',4],name='xiaowu', age=18)
    #
    # l = [1,'2',False]
    # d = {'name': 'xiaoming', 'age': '16'}
    # example_dynamic_args(*l, **d)
    # print(anonymous_fuc(3))
    # print(equals_anonymous_fuc(3))
    # magic3()
    # magic4()
    # magic5()
    # magic6()
    # magic7()
    # magic8()

    ep = example_generator([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7])
    print(next(ep))
    # test_generator2()

    # foo_test2()
    # foo2_test3()

    # ed = example_decorator2(func)
    # ed()


if __name__ == '__main__':
    main()
