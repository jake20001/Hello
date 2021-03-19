# -*- encoding: utf-8 -*-
"""
@File    : test_prestr.py
@Time    : 2020/9/12 14:14
@Author  : Aaron Liao
"""
import itertools
from typing import List

def permutation(str):
    """
    引用permutation函数计算任意变换子集
    :param str:
    :return:
    """
    s = list(str)
    result = []
    status = False
    for i in range(len(s)+1,0,-1):
        res = itertools.permutations(s,i)
        print(res)
        res = {''.join(line) for line in res}
        for r in list(res):
            if r == r[::-1]:
                ##print(len(r))
                ##以上可知道回文字符串长度，以下为找到回文##
                result.append(r)
                status = True
        if status:
            break
    # print(result)
    for r in result:
        re = itertools.permutations(r)
        re = {''.join(line) for line in re}
        for e in list(re):
            if e in str:
                print("最长回文字符串为：",e,"回文==>",r,"长度为",len(r))

permutation("9498331")

