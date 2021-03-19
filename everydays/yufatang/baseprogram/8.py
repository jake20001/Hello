# coding: utf-8
"""
    @author: zhangjk
    @file: 2.py
    @date: 2020-02-28
    说明：输入输出; 文件读写
"""
from io import BytesIO


def f1():
    # s = 'Hello, Runoob'
    s = {"aaa":1}
    print(s,type(s))
    print(str(s))
    print(repr(s),type(repr(s)))
    print(str(s)==repr(s))
    print(eval(repr(s)),type(eval(repr(s))))
    print(s==eval(repr(s)))


def f2():
    # 打开一个文件
    f = open("foo.txt", "w")
    f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
    # 关闭打开的文件
    f.close()

def f3():
    # 打开一个文件
    f = open("foo.txt", "r")
    f.seek(2)
    str = f.read()
    print(str)
    print(len(str))
    print(f.tell())
    # str = f.readline()
    # str = f.readlines()


    # 关闭打开的文件
    f.close()

def f4():
    # 打开一个文件
    f = open("foo.txt", "r")

    for line in f:
        print(line, end='')

    # 关闭打开的文件
    f.close()


def f5():
    import pickle

    # 使用pickle模块将数据对象保存到文件
    data1 = {'a': [1, 2.0, 3, 4+6j],
             'b': ('string', u'Unicode string'),
             'c': None}

    selfref_list = [1, 2, 3]
    selfref_list.append(selfref_list)
    # print(selfref_list)

    output = open('data.pkl', 'wb')

    # Pickle dictionary using protocol 0.
    pickle.dump(data1, output)

    # Pickle the list using the highest protocol available.
    pickle.dump(selfref_list, output, -1)

    output.close()

def f6():
    import pprint, pickle

    #使用pickle模块从文件中重构python对象
    pkl_file = open('data.pkl', 'rb')
    print(type(pkl_file))
    # data1 = pickle.load(pkl_file)
    # pprint.pprint(data1)
    # data2 = pickle.load(pkl_file)
    # pprint.pprint(data2)

    data3 = pickle.loads(pkl_file.read(),encoding='bytes')
    pprint.pprint(data3)

    pkl_file.close()


f1()
# f2()
# f3()
# f4()
# f5()
# f6()


