# coding: utf-8
"""
    @author: zhangjk
    @file: 16.py
    @date: 2020-02-28
    说明：dict
"""

def f1():
    dict = {}
    dict['one'] = "python"
    dict[2] = "java"

    tinydict = {'name': 'python','code':1, 'company': 'beantechs'}
    print(tinydict.items().isdisjoint({'pastman':2}))
    print(tinydict.items().isdisjoint({'code':1}.items()))
    print(tinydict.items().isdisjoint(['code']))

    print (dict['one'])       # 输出键为 'one' 的值
    print (dict[2])           # 输出键为 2 的值
    print (tinydict)          # 输出完整的字典
    print (tinydict.keys())   # 输出所有键
    print (tinydict.values()) # 输出所有值

def f2():
    a = dict([('Python', 1), ('Java', 2), ('C', 3)])
    print(a)

    b = {x: x**2 for x in (2, 4, 6)}
    print(b)

    c = dict(Python=1, Java=2, C=3)
    print(c)

def f3():
    a = dict([('Python', 1), ('Java', 2), ('C', 3)])
    print(a)
    a.clear()
    print(a)
    a['JK'] = 1
    a['Tom'] = 2
    a['Jane'] = 3
    print(a)
    b = a.get('JK')
    print(b)
    a.pop('Tom')
    print(a)
    for key,value in a.items():
        print(key,value)

def f4():
    a = ['python','java','c']
    b = set([1,2,3])
    c = [1,2,3]
    z = dict.fromkeys(a,b)
    cz = dict.fromkeys(a,c)
    # print(z)
    print(cz)


def main():
    f1()
    # f2()
    # f3()
    # f4()


if __name__ == '__main__':
    main()