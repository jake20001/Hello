# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/5/18 16:06
# FileName : 4
# Description : 
# --------------------------------
from typing import List, Generator

ax = []
def MainPrint(s, t, predecessor):
    for n in print_path2(s, t, predecessor):
        if n == t:
            print(t)
        else:
            print(n, end=' -> ')

def print_path(s: int, t: int, p: List[int]) -> Generator[int, None, None]:
    if t == s:
        yield s
    else:
        yield from print_path(s, p[t], p)
        yield t
        print('t ==>',t)

def print_path2(s: int, t: int, p: List[int]) -> Generator[int, None, None]:
    if t == s:
        yield s
    else:
        # s = list(print_path2(s,p[t],p))
        # print('s -->',s)
        # yield s
        return list(print_path2(s,p[t],p))
        yield t



def main():
    ax = [-1, 0, 3, 1, 0, 2]
    MainPrint(0,5,ax)

if __name__ == '__main__':
    main()