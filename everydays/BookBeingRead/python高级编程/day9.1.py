# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/17 15:29
# FileName : day9.1
# Description : 
# --------------------------------

from bisect import bisect


def find(seq,el):
    pos = bisect(seq,el)
    if pos==0 or (pos==len(seq) and seq[-1]!=el):
        return -1
    return pos-1

# seq = [2,3,7,8,9]
# print(find(seq,9))

seq = ['a','a','b','c','c','c','d']
# print(seq.count('a'))

def find_one_count():
    res = []
    std = set()
    for el in seq:
        if el not in res:
            if el in std:
                continue
            res.append(el)
        else:
            res.remove(el)
            std.add(el)
    return res,std

# print(find_one_count())


