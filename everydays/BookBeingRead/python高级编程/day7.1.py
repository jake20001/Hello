# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/5 14:26
# FileName : day7.1
# Description : 
# --------------------------------

# 常量：全意思的大写 ： REPORT_ONLY_FIRST_FAILURE
# 公有变量：小写  observers
# 私有变量：__小写  __observers
# 公有方法：全小写 secret
# 私有方法：__全小写 __secret
# 特殊方法: __小写__  __str__
# 属性：_小写 _connected
# 类：第一个大写word*n（重复） CamelCase
# 模块和包：小写 os
# 判断：is_名称 或者 has_名称  is_connected 或者 has_connected
# 复数：名称s  connected_users

class DemoCase(object):

    REPORT_ONLY_FIRST_FAILURE = 'fail'
    observers = 1
    # 私有无法直接在类外访问
    __observers = 2
    _connected = []

    def __init__(self):
        self.me = 'What is test?'

    def __str__(self):
        return self.me

    def get_observers(self):
        return DemoCase.__observers

    def __secret(self):
        return self

    def secret(self):
        return self.__secret()

    def connect(self,user):
        self._connected.append(user)

    def _connect_people(self):
        return '\n'.join(self._connected)

    connected_people = property(_connect_people)



def main():
    mtest = DemoCase()
    # print(test.REPORT_ONLY_FIRST_FAILURE)
    # print(test.observers)
    # print(test.__observers)
    # print(mtest.get_observers())
    # print(mtest.__secret)
    # print(mtest.secret())
    mtest.connect('Tarek')
    mtest.connect('Shannon')
    print(mtest.connected_people)



if __name__ == '__main__':
    main()


