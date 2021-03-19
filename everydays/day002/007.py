# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 14:58
# FileName : 007
# Description : 
# --------------------------------
def fa():
    ax = []
    ax.append('a')
    return ax

def fb():
    bx = []
    bx.append('b')
    bx.append('c')
    return bx

def main():
    print(*fa())
    print(*fb())
    print([*fa(),*fb()])

if __name__ == '__main__':
    main()
