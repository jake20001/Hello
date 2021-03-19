# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/9/4 15:17
# FileName : yyj2
# Description : 
# --------------------------------

a = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def path(a, m):
    for i in range(len(a[m])):
        a[m][i] += min(a[m + 1][i], a[m + 1][i + 1])
        print(i,a[m][i])
    if m > 0:
        path(a, m - 1)
    return a


path(a, len(a) - 2)
print(a[0][0])