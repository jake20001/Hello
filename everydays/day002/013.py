# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : Hello
# Author : zhangjk
# CreateTime : 2021/3/17 18:27
# FileName : 013
# Description : 
# --------------------------------

# [1,2]
# [1] ,[2],[1,2]   C2-1 + c2-2 = 2+1 = 3

# [1,2...n]
# Cn1 + cn2 + ... + Cnn = >  Cn0 + Cn1 + .. + Cnn = 2^n
# Sn = 2^n-1

def calc(data):
    print('calc')
    l = len(data)
    print("ll",l)
    flag = []
    count = 0
    for i in range(l):
        flag.append(0)
    # print(flag)
    while True:
        for i in range(0,l):
            if flag[i]==0:
                flag[i] = 1
                continue
            else:
                flag[i] = 0
                break
        for i in range(l):
            if flag[i]==1:
                print(data[i], end=' ')
        print()
        if 1 not in flag:
            break
        count = count+1
    print("count",count)


def AA():
    for i in range(6,10,2):
        print(i)




def main():
    ax = [1,2,3,4,5,6]
    calc(ax)
    # AA()


if __name__ == '__main__':
    main()