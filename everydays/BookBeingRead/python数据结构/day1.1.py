# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/18 16:49
# FileName : day1.1
# Description : iterator
# --------------------------------

class _BagIterator(object):
    def __init__(self,the_list):
        self._the_list = the_list
        self._cur_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_item<len(self._the_list):
            item = self._the_list[self._cur_item]
            self._cur_item += 1
            return item
        else:
            raise StopIteration

bag = _BagIterator([11,22,33,44])
# for i in range(4):
#     print(next(bag))
for b in bag:
    print(b)


