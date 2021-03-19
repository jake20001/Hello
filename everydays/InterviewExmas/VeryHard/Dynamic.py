# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/7/4 14:16
# FileName : Dynamic
# Description :
#
# --------------------------------

def PrintAX2():
    ax = [7,3,8,8,1,0,2,7,4,4,4,5,2,6,5]
    k = 0
    ii = 0
    for i in range(k+ii,len(ax)):
        for j in range(k+ii,k+ii+i+1):
            print(ax[j],end=' ')
        print()
        ii = 2*i+1

def PrintAX1():
    ax = [7,3,8,8,1,0,2,7,4,4,4,5,2,6,5]
    k = 0
    indx = 0
    isBreak = False
    for i in range(len(ax)):
        if isBreak:
            break
        for j in range(i+1):
            try:
                print(ax[k],end=' ')
                k += 1
            except:
                isBreak = True
        indx += 1
        print()
    return indx


def PrintAX():
    ax = [7,3,8,8,1,0,2,7,4,4,4,5,2,6,5,1]
    c = 0
    for i in range(len(ax)):
        bx = ax[c:c+i+1]
        c = c + i+1
        if not bx:
            break
        print(bx)







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
    print(bxx)
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
        # ew[i][j][list(ew[i][j].keys())[0]] = max(one,two) + list(ew[i][j].keys())[0]
        ew[i][j][list(ew[i][j].keys())[0]] = min(one,two) + list(ew[i][j].keys())[0]
    return ew[i][j][list(ew[i][j].keys())[0]]


def main():
    # PrintAX()
    print(MaxSum(erweijuzhen(),0,0))

if __name__ == '__main__':
    main()
