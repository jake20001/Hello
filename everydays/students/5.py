# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/8/24 16:55
# FileName : 5
# Description : 
# --------------------------------

def path2(n, num):
    a = [n - 1, n - 2, n - 3]
    for i in a:
        print('yyy',i)
        if i == 0:
            num += 1
        elif i > 0:
            num = path(i, num)
            # print("xxx",i)
        # else:
        #     break
    return num

def path(n,num,s):
    a=[n-1,n-2,n-3]
    for i in range(3):
        if a[i]==0:
            s.append(i + 1)
            num+=1
            print(s)
            s.pop()
        elif a[i]>0:
            s.append(i + 1)
            num=path(a[i],num,s)
        else:
            break
    if s!=[]:
        s.pop()
    return num



def main():
    # count = 0
    # print(path(3, count))

    count=0
    s=[]
    print(path(5,count,s))
    print(s)


if __name__ == '__main__':
    main()
