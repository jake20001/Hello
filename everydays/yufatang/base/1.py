# coding: utf-8
"""
    @author: zhangjk
    @file: str2excel.py
    @date: 2020-02-28
    说明：字符串 string
"""
import builtins
import keyword

# print(keyword.kwlist)
# print(keyword.iskeyword)

def aa():
    total = 'item_one' + \
            'item_two' + \
            'item_three'

    print(total)

def bb():
    total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

    print(total)

def cc():
    a = 1 + 2j
    b = 1 - 2j
    c = 2 - 3j
    print(a*b)
    print(a*c)


def dd():
    nstr = 'Python'
    print(nstr)
    print(id(nstr))
    nstr = nstr + "算法"
    print(nstr)
    print(id(nstr))

    ystr = xstr = 'Python'
    print(id(xstr))
    print(id(ystr))

    print(nstr)                 # 输出字符串
    print(nstr[0:-1])           # 输出第一个到倒数第二个的所有字符
    print(nstr[0])              # 输出字符串第一个字符
    print(nstr[2:5])            # 输出从第三个开始到第五个的字符
    print(nstr[2:])             # 输出从第三个开始后的所有字符
    print(nstr * 2)             # 输出字符串两次
    print(nstr + '你好')        # 连接字符串
    print('------------------------------')
    print('hello\n' + nstr)      # 使用反斜杠(\)+n转义特殊字符
    print(r'hello\n' + nstr)     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


def ee():
    print(dir(str))

def ff():
    a = 1
    print(globals())

def g1():
    a = 1
    print(locals())

def g2():
    print(dir(builtins))

def g3():
    import sys
    x = 'runoob'
    sys.stdout.write(x + '\n')

def main():
    # ee()
    # ff()
    # g1()
    # g2()
    # dd()
    g3()


if __name__ == '__main__':
    main()