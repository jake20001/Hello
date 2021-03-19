# coding: utf-8
"""
    @author: zhangjk
    @file: 9.py
    @date: 2020-02-28
    说明：文件/目录方法
"""

import os, sys


def f1():
    # 使用 mkdir 命令
    # cmd = 'cd. > 1.txt'
    cmd = 'echo hello > 2.txt'
    # cmd = 'md world > 3.txt'
    # cmd = 'type world > 4.txt'
    os.system(cmd)
    # cmd = '1.txt'
    # b = os.popen('notepad 2.txt','r').read()
    # print(b)
    bx = open('2.txt','r').read()
    print(bx)

def f2():
    for f in os.listdir():
        if os.path.isdir(f):
            continue
        print(f)


def main():
    f1()


if __name__ == '__main__':
    main()