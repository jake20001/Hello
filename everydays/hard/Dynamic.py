# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/7/4 14:16
# FileName : Dynamic
# Description : 
# --------------------------------

def erweijuzhen():
    bxx = []
    ax = [7,3,8,8,1,0,2,7,4,4,4,5,2,6,5]
    n = 5
    k = 0
    for i in range(1,6):
        tx = []
        for j in range(1,i+1):
            td = {}
            td[ax[k]] = -1
            tx.append(td)
            k += 1
        bxx.append(tx)
    return bxx

def MaxSum(ew,i,j):
    print(list(ew[i][j].keys())[0])
    if ew[i][j][list(ew[i][j].keys())[0]]!=-1:
        return ew[i][j][list(ew[i][j].keys())[0]]
    if i==len(ew)-1:
        ew[i][j][list(ew[i][j].keys())[0]] = list(ew[i][j].keys())[0]
    else:
        one = MaxSum(ew,i+1,j)
        two = MaxSum(ew,i+1,j+1)
        ew[i][j][list(ew[i][j].keys())[0]] = max(one,two) + list(ew[i][j].keys())[0]
    return ew[i][j][list(ew[i][j].keys())[0]]


def main():
    print(MaxSum(erweijuzhen(),0,0))

if __name__ == '__main__':
    main()
