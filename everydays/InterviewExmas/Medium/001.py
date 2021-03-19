# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/6/23 9:53
# FileName : 1
# Description : 
# --------------------------------
from queue import Queue


def ysf():
    q = Queue()
    for i in range(3):
        dic = {}
        dic[i + 1] = i + 1
        q.put(dic)

    while True:
        if q.qsize() == 1:
            print(q.get())
            return
        item = q.get()
        print(item.keys(),type(item.keys()))
        k = list(item.keys())[0]
        if k % 2 != 0:
            item[q.qsize()+1] = list(item.values())[0]
            del item[k]
            q.put(item)

def ysf1():
    dic = {}
    for i in range(6):
        dic[i + 1] = i + 1
    while True:
        if len(dic) == 1:
            print(dic)
            return
        l = len(dic)
        for index in list(dic.keys()):
            if index%2==1:
                dic[l+index] = dic[index]
                l = l-1
            del dic[index]


def main():
    ysf1()


if __name__ == '__main__':
    main()
