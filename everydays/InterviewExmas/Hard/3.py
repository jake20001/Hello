# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/8/4 15:25
# FileName : 3
# Description : 如果有n级台阶，每次只能走1格或者2格，有多少种走法
# --------------------------------

# 对于n值的0,1数组组合
def GetNCombine(n):
    count = 0
    ax = []
    for i in range(n):
        ax.append(0)

    bx = []
    while True:
        for i in range(n):
            if ax[i] == 0:
                ax[i] = 1
                continue
            else:
                ax[i] = 0
                break
        sx = []
        for i in range(n):
            # print(ax[i],end=' ')
            sx.append(str(ax[i]))
            cx = ''.join(sx)
        bx.append(cx)
        # print()
        if 1 not in ax:
            break
        count = count+1
    return bx

def GetKindsCount(bx):
    # 0 为1步
    # 11 为2步
    dt = {'11':'B','0':'A'}
    ax = []
    for i in range(len(bx)):
        s = ''
        isJump = False
        isNOOK = True
        for j in range(len(bx[i])):
            if isJump:
                isJump = False
                continue
            if bx[i][j]=='0':
                s += dt['0']
            elif bx[i][j]=='1':
                if j+1==len(bx[i]):
                    print("越界")
                    s += '1'
                    isNOOK = False
                    break
                if bx[i][j+1]=='0':
                    print("没有这种走法")
                    isNOOK = False
                    break
                else:
                    s += dt['11']
                    isJump = True
        print('s',s)
        if isNOOK:
            ax.append(s)
    return ax

def GetRightAnswer(dx):
    dt = {'A':'0','B':'11'}
    ax = []
    for d in dx:
        s = ''
        for i in range(len(d)):
            s += dt[d[i]]
        ax.append(s)
    return ax



def main():
    bx = GetNCombine(5)
    print(bx)
    dx = GetKindsCount(bx)
    print(dx)
    print(GetRightAnswer(dx))



if __name__ == '__main__':
    main()