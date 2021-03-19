# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/3 16:02
# FileName : day3.2
# Description : 
# --------------------------------

class User(object):
    def __init__(self,roles):
        self.roles = roles

class Unauthorized(Exception):
    pass

def inroles(irole,roles):
    for role in irole:
        if role in roles:
            return True
    return False

def protect(irole):
    def _protect(function):
        def __protect(*args,**kwargs):
            user = globals().get('user')
            if user is None or not inroles(irole,user.roles):
                raise Unauthorized("I won't tell you")
            return function(*args,**kwargs)
        return __protect
    return _protect

def protect2(role):
    def _protect(function):
        def __protect(*args,**kwargs):
            user = globals().get('user')
            if user is None or role not in user.roles:
                raise Unauthorized("I won't tell you")
            return function(*args,**kwargs)
        return __protect
    return _protect

tarek = User(('admin','user'))
bill = User(('user',))
visit = User(('visit',))

class MySecrets(object):
    @protect(['admin','user'])
    def waffle_recipe(self):
        print('use tons of butter')

these_are = MySecrets()
user = tarek
these_are.waffle_recipe()
user = bill
these_are.waffle_recipe()
user = visit
these_are.waffle_recipe()