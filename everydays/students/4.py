# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/8/22 15:59
# FileName : 4
# Description : 
# --------------------------------
import copy


def testcopy():
    ax = [1,2,3]
    bx = [x for x in ax]
    print(ax)
    print(bx)
    ax[0] = 100
    print(ax)
    print(bx)

def strtest():
    s = 'aaa'
    print(id(s))
    s = s + 'bbb'
    print(id(s))
    # b = 'aaa'
    # c = 'aac'
    # # d = 'aa' + 'c'
    # print(id(s))
    # print(id(b))
    # print(id(c))
    # # print(id(c))
    # e = c + 'dd'
    # print(id(e))
    # f = e + 'ee'
    # print(id(f))
    # ax = [1,2]
    # bx = [1,2]
    # print(id(ax))
    # print(id(bx))
    # print(id(s))
    # s = s.replace('a','b',2)
    # print(id(s))

    # print(id(s))
    # # s = list(s)
    # # print(s[0])
    # # s[0] = 's'
    # # print(s)
    # # s = s.split(',')
    # # s[0] = 's'
    # # print(s)
    # # s = s + 'bbb'
    # # print(id(s))
    #
    # # s = copy.deepcopy(s)
    # # print(id(s))
    # s = s + 'ccc'
    # print(id(s))
    #
    # # s = copy.copy(s)
    # print(id(s))
    # s = s + 'dddd'
    # print(id(s))





def main():
    # testcopy()
    strtest()


if __name__ == '__main__':
    main()
