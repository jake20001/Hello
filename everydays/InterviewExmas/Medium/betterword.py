# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/9/12 12:15
# FileName : betterword
# Description : 给你一个字符串s，请返回s中最长的超赞子字符串的长度
#               超赞字符串满足条件：
#               1，该字符串非空
#               2，进行任意交换字符后，该字符串可以变成一个回文字符串
# --------------------------------
import itertools


class Demo(object):

    def __init__(self):
        self.nums = 0
        self.axx = []

    def isMax(self):
        return max([1, 2, 4])

    def son_good_word(self, nstr):
        length = -1
        for i in range(len(nstr)):
            for j in range(i + 1, len(nstr) + 1):
                son = nstr[i:j]
                # print("字符串：", son)
                if self.good_word(son):
                    length = max(len(son), length)
        return length


    def permutation(self,nx,p,q):
        if p==q:
            # print(nx)
            self.nums += 1
            if nx not in self.axx:
                self.axx.append(nx)
        else:
            for i in range(p,q):
                nx[i], nx[p] = nx[p], nx[i]
                self.permutation(nx, p+1, q)
                nx[i], nx[p] = nx[p], nx[i]

    def pailie(self,nstr):
        nx = list(nstr)
        res = itertools.permutations(nx,len(nx))
        print(list(res))



    # 超赞字符串:奇数个字符的只有一种或者没有
    def good_word(self,nstr):
        # res = itertools.permutations(nstr,len(nstr))
        # print(list(res))
        self.permutation(list(nstr),0,len(list(nstr)))
        for x in self.axx:
            if x==x[::-1]:
                return True
        return False

    def good_word2(self, nstr):
        nlist = list(nstr)
        ax = []
        for n in nlist:
            if n not in ax:
                ax.append(n)
        # 统计每个字符的个数
        mDict = {}
        for i in range(len(ax)):
            mDict[ax[i]] = 0
        for i in range(len(nlist)):
            for j in range(len(ax)):
                if ax[j] == nlist[i]:
                    mDict[ax[j]] += 1
        # for key,value in mDict.items():
        bx = list(mDict.values())
        index = 0
        for i in range(len(bx)):
            if bx[i] % 2 == 1:
                index += 1
        if index == 0 or index == 1:
            return True
        return False


    def testsum2(self,nstr):
        n = nstr.count('a')
        print(n)

    def testsum(self,value):
        return sum(1 for v in self if v is value or v == value)

    # 把数字成对成对删除
    def is_good_words(self,nstr):
        nlist = list(nstr)
        i = 0
        while i<(len(nlist)):
            j = i+1
            while j<len(nlist):
                if nlist[i]==nlist[j]:
                    nlist.remove(nlist[i])
                    nlist.remove(nlist[j-1])
                    print(nlist)
                    i=0
                    break
                j += 1
            i += 1
        print(nlist)

def main():
    mDemo = Demo()
    mDemo.is_good_words('abbccddcdcd')
    # print("这是超赞字符:",mDemo.good_word2('abbccddc'))
    # print(mDemo.isMax())
    # print("最长超赞字符串:", mDemo.son_good_word("abbccdd"))
    # # mDemo.pailie('abbc')
    # # mDemo.permutation(list('abbc'),0,len(list('abbc')))
    # # print(mDemo.nums)
    # # print(mDemo.axx)
    # # print(mDemo.testsum('axa'))


if __name__ == '__main__':
    main()
