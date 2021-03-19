# coding: utf-8
"""
    @author: zhangjk
    @file: 3.py
    @date: 2020-02-28
    说明：list
"""

def f1():
    list = [ 'C Program', 'Java Program', 'Python Program' ]
    tinylist = ['Cat', 'Snake']

    print (list)            # 输出完整列表
    print (list[0])         # 输出列表第一个元素
    print (list[1:3])       # 从第二个开始输出到第三个元素
    print (list[2:])        # 输出从第三个元素开始的所有元素
    print (tinylist * 2)    # 输出两次列表
    print (list + tinylist) # 连接列表

def f2():
    tinylist = ['Cat', 'Snake']
    print(id(tinylist))
    tinylist.append('Shark')
    print(tinylist)
    print(id(tinylist))
    tinylist = tinylist + ['Shark']
    print(tinylist)
    print(id(tinylist))


def f3():
    letters = ['p','y','t','h','o','n']
    print(id(letters))
    print(letters[::2])
    ls = letters[::2]
    print(id(ls))
    print(id(letters[::2]))
    print(letters)
    print(id(letters))

def f4():
    a = max(['p','y','t','h','o','n'])
    b = max([1,23,4])
    print(a)
    print(b)


def main():
    # f1()
    # f2()
    # f3()
    f4()



if __name__ == '__main__':
    main()
