# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/6/13 11:12
# FileName : 6
# Description : 约瑟夫环问题
# --------------------------------


def count(n):
    peoples = {}
    for i in range(1,n+1):
        peoples[i] = i
    return peoples

def ysfh(peoples,m):
    if len(peoples)==1:
        print(peoples)
        return
    for index in list(peoples.keys()):
        if index%m!=0:
            peoples[len(peoples)+index] = peoples[index]
        peoples.pop(index)
    # print(peoples)
    ysfh(peoples,m)

def ysfdg(xsum, value, n):
    if ( n == 1 ):
        return (xsum + value-1) %xsum
    else:
        return (ysfdg(xsum-1,value,n-1) + value) %xsum

def f1():
    #控制参数：
    nums = 6
    call = 2
    #参数定义：
    peoples = []
    for _ in range(nums):
        peoples.append(True)
    result = []
    num =1
    #主逻辑
    while(any(peoples)):
        for index,people in enumerate(peoples):
            if people:
                if num == call:
                    peoples[index] = False
                    result.append(index+1)
                    #                print(index+1)#每轮的出局者
                    #                print(peoples)#每次的队列状态
                    num = 1
                else:
                    num += 1
    print('-'* 25)
    print('\n总数为%d,报数为%d' % (nums,call))
    print('约瑟夫序列为：\n%s\n' % result)
    print('-'* 25)


from queue import Queue


def ysf():
    q = Queue()

    for i in range(6):
        q.put(i+1)

    index = 1
    while True:
        if q.qsize()==1:
            print(q.get())
            return
        item = q.get()
        if index==2:
            index = 1
        else:
            index += 1
            q.put(item)
            print(q.queue)


def is_palindrome(n):
    b=str(n)
    if b[::-1] == b:
        return int(b)
    else:
        return


def f21():
    n = str(78)
    print(n[::-1])


def main():
    # for p in range(1,51):
    # ysfh(count(6),2)
    # for i in range(1,6+1):
    #     print(ysfdg(6,2,i))
    # f1()
    ysf()
    # output = filter(is_palindrome, range(1, 100))
    # print(output)
    # for i in output:
    #     print(i)
    # print(list(output))
    # f21()



if __name__ == '__main__':
    main()


