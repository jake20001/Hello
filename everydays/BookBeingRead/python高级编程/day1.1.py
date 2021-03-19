# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/11/26 15:06
# FileName : day1
# Description : 列表推导
# --------------------------------

# 获取数据中所有偶数值
def f1():
    return [i for i in [1,2,3,4,5,6] if i%2==0]

# print(f1())


# enumerate
def f2():
    ax = ['one','two','three']
    return [(x,y) for x,y in enumerate(ax)]

print(f2())


