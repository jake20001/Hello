# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/18 17:09
# FileName : day1.2
# Description : Array2D
# --------------------------------
import ctypes


class Array(object):
    def __init__(self,size):
        assert size>0,"Array size must be > 0"
        self.size = size
        PyArrayType = ctypes.py_object*size
        self._elments = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert index>=0 and index<len(self),"Array out of range"
        return self._elments[index]

    def __setitem__(self, index, value):
        assert index>=0 and index<len(self),"Array out of range"
        self._elments[index] = value

    def __iter__(self):
        return _ArrayIterator(self._elments)

    def clear(self,value):
        for i in range(len(self)):
            self._elments[i] = value

class _ArrayIterator(object):
    def __init__(self,the_array):
        self._the_array = the_array
        self._cru_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cru_index<len(self._the_array):
            entry = self._the_array[self._cru_index]
            self._cru_index += 1
            return entry
        else:
            raise StopIteration


class Array2D(object):

    def __init__(self,rows,clos):
        self._t_rows = Array(rows)
