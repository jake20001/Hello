# -*- encoding: utf-8 -*-
"""
@File    : businees.py
@Time    : 2020/9/27 18:58
@Author  : Aaron Liao
"""
def businees1():
    """
    不考虑限制条件，即可以囤货出售
    :return:
    """
    a = [2,3,1,5,3,6,1,4,6,2,3,4,1,9,6,2,1,8,7,4,3,5,4,7,6,2]
    max_dir = {}
    for i in range(len(a)):
        max_enable = []
        maxi = 0
        for j in a[i:]:
            if j - a[i] > 0:
                max_enable.append(j)
        if max_enable:
            for d in max_enable:
                maxi += d - a[i]
        max_dir['第'+str(i+1)+'天买进' + str(len(max_enable))+ '支股票'] = maxi
    # print(max_dir.values())
    for k in max_dir.keys():
        if max_dir[k] == max(max_dir.values()):
            print(k,"最大收益为：",max(max_dir.values()))

def businees2():
    """
    限制：购买前出售之前的股票
    :return:
    """
    a = [2,3,50,12,100,11]
    max_dir = {}
    maxi = 0
    for i in range(1,len(a)):
        if a[i] - a[i-1] > 0:
            maxi += a[i] - a[i-1]
    return maxi

print(businees2())
