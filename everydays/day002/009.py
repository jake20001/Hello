# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 15:11
# FileName : 009
# Description : 
# --------------------------------

import sys

class Demo(object):

    def __init__(self):
        pass

    def f1(self):
        while True:
            line = sys.stdin.read(1)
            # print(line)
            if line=='q':
                break
            sys.stdout.write(line + '\n')
            sys.stdout.flush()

def main():
    mDemo = Demo()
    mDemo.f1()


if __name__ == '__main__':
    main()
