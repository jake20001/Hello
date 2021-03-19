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
    cmd = 'mkdir nwdir'
    b = os.popen(cmd,'r',1)
    print(b)


def f2():
    for f in os.listdir():
        if os.path.isdir(f):
            continue
        print(f)


f2()