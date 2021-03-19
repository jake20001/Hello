# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/5/22 10:49
# FileName : 5
# Description : 
# --------------------------------

# 列表推导式
def f1():
    td_list = [i for i in range(10)]
    print(td_list)

# 词典推导式
def f2():
    import random
    def getNum(i):
        return i
    td_dict = {k:getNum(ord(k)) for k in ['a','b','c','d']}
    print(td_dict)

# 生成器
def f3():
    ge_list = (i for i in range(10))
    print(ge_list)
    print(list(ge_list))

def f4():
    t_list = ['ab','abc','ad','ac','aw','az','a','jdajdj']
    b = sorted(t_list,key=lambda x:(len(x),x))
    print(b)

# 字母排序,先排序长度,再排序字母大小
def SortStrings():
    t_list = ['jdajdj','ab','abc','ad','ac','aw','az','a']
    for i in range(len(t_list)):
        l = len(t_list[i])
        for j in range(i+1,len(t_list)):
            lj = len(t_list[j])
            if l>lj:
                t_list[i],t_list[j] = t_list[j],t_list[i]
    print(t_list)
    return
    c_list = []
    for i in range(len(t_list)):
        for j in range(i+1,len(t_list)):
            if len(t_list[i])<len(t_list[j]):
                break
            if not comparTwo(t_list[i],t_list[j]):
                t_list[i],t_list[j] = t_list[j],t_list[i]
        c_list.append(t_list[i])
        # t_list.remove(t_list[i])
    print(c_list)

    # for i in range(len(t_list)-1):
    #     ci = t_list[i]
    #     di = t_list[i+1]
    #     if len(ci)<len(di):
    #         c_list.append(ci)
    #     else:
    #         if comparTwo(ci,di):
    #             pass
    #         else:
    #             ci,di = di,ci
    #         c_list.append(ci)
    # print(c_list)

def comparTwo(a,b):
    for i in range(len(a)):
        if a[i]<b[i]:
            return True
    return False


def f6():
    import re
    s = "info:xiao 33 shan"
    res = re.split(r':| ',s)
    print(res)
    email_list = ['xiao@163.com','xiao@163.comx.cn','xiao@qq.com']
    for email in email_list:
        ret = re.match("(.*)+@163\.com$",email)
        if ret:
            print(ret.group())


def f7():
    import json
    dic = {'name':'zs'}
    res = json.dumps(dic)
    print(res,type(res))
    ret = json.loads(res)
    print(ret,type(ret))

def f8():
    nstr = "dad mm dad aunt dad"
    res = nstr.count('dad')
    print(res)
    ret = nstr.center(10,'A')
    print(ret)

def f9():
    import re
    tels = ['13223242324','13223242329','13223242327','10086']
    pattern = '1\d{9}[^47]'
    for tel in tels:
        ret = re.match(pattern,tel)
        if ret:
            print(ret.group())

def SortStrings2():
    t_list = ['jdajdj','ab','abc','ad','ac','aw','az','a']
    for i in range(len(t_list)-1):
        for j in range(len(t_list)-i-1):
            if len(t_list[j])>len(t_list[j+1]):
                t_list[j],t_list[j+1] = t_list[j+1],t_list[j]
            elif len(t_list[j])<len(t_list[j+1]):
                pass
            else:
                if t_list[j]>t_list[j+1]:
                    t_list[j],t_list[j+1] = t_list[j+1],t_list[j]
    print(t_list)

def main():
    # f1()
    # f2()
    # f3()
    # f4()
    # SortStrings()
    # f6()
    # f7()
    # f8()
    # f9()
    SortStrings2()


if __name__ == '__main__':
    main()