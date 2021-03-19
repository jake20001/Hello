# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/3 17:33
# FileName : day4.1
# Description : 
# --------------------------------

class DistinctError(Exception):
    pass

class distinctdict(dict):

    def __setitem__(self, key, value):
        try:
            value_index = list(self.values()).index(value)
            existing_key = list(self.keys())[value_index]
            if existing_key!=key:
                # raise DistinctError("this value already exists for %s" % self[existing_key])
                print("this value already exists for %s" % self[existing_key])
        except ValueError:
            pass
        super(distinctdict,self).__setitem__(key,value)

my = distinctdict()
my['key'] = 'value'
my['other_key'] = 'value'
my['other_key'] = 'value2'
print(my)
