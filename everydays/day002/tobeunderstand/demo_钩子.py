# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/3/13 15:43
# FileName : demo_钩子
# Description : 
# --------------------------------

import pluggy

#创建规范装饰器
hookspec = pluggy.HookspecMarker('aaa')
#创建插件类装饰器
hookimpl = pluggy.HookimplMarker('aaa')


class MySpec():
    # firstresult=True设置之后，等到第一个返回非空结果的hookimpl，就返回（hookwrapper还是正常执行）
    @hookspec()
    def myhook(self, arg_one, arg_two):
        print("MySpec ...")
        pass

class MyPlugin():
    # tryfirst=True,trylast=True定义执行顺序
    @hookimpl()
    def myhook(self, arg_one):
        print('MyPlugin,arg_one%s'%(arg_one))
        return arg_one

class MyPluginOther():
    @hookimpl()
    def myhook(self, arg_one, arg_two):
        print('MyPluginOther,arg_one%s arg_two%s'%(arg_one,arg_two))
        return arg_one, arg_two

class MyPluginWrapper():
    '''
    hookwrapper作为每个钩子函数的上下文运行
    在所有hook之前先运行
    '''
    @hookimpl(hookwrapper=True)
    def myhook(self):
        print('--------  hool wrapper before -----------')

        # 生成器会给outcome send一个pluggy.callers._Result对象
        outcome = yield

        print('--------  hook wrapper after -----------')
        # 通过get_result拿到所有钩子函数的结果
        res = outcome.get_result()
        print('get all hook return ', res)
        # 强制更改钩子函数返回结果
        outcome.force_result(1)

        print('-------- hook wrapper end-----------')

#用于把构建注册到test1，然后test1统一调用myhook钩子函数，收集钩子函数的return结果 'aaa'为project_name要统一
test1 = pluggy.PluginManager('aaa')
test1.add_hookspecs(MySpec)

# 后注册的先执行，收集进结果
test1.register(MyPlugin())
test1.register(MyPluginOther())
test1.register(MyPluginWrapper())

# hookimpl调用，必须用关键字语法
result = test1.hook.myhook(arg_one=1, arg_two=2)
print(result)