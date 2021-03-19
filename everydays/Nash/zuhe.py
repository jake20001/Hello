# coding : utf-8
'''
    @author :  zhang.jianke
    @project:  WorkSpaceDemo
    @file   :  zuhe.py
    @date   :  2020-04-06
'''

class Zuhe(object):

    def __init__(self):
        self.resx = []
        self.ax = [1,2]

    def subsets3(self):
        self.helper(0,[])
        print(self.resx)


    def helper(self,i, tmp):
        if tmp!=[]:
            self.resx.append(tmp)
        for j in range(i, len(self.ax)):
            self.helper(j + 1,tmp + [self.ax[j]])


    def subsets2(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res


    def subsets(self, nums):
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]])
        helper(0, [])
        return res




    def GetSon(self,res):
        for num in res:
            return num

    def f1(self):
        print([] + [1])



def main():
    mZuhe = Zuhe()
    # mZuhe.f1()
    # return
    res = mZuhe.subsets3()



if __name__ == '__main__':
    main()





# #include <stdio.h>
# #include <stdlib.h>
#
# void printArray(int* a, int length)
# {
#     printf("[ ");
# for (int i = 0; i < length; i++)
# printf("%d ", a[i]);
# printf("] ");
# }
# void printCombination(int*a, int n, int m,int k,int*p,int plength)
# {
#     int i = 1;
# int j = 0;
# if (m == 1)
# {
# for (int ii = 0; ii < n - 1; ii++)
# {
#     *(p+k) = *(a + 1 + ii);
# printArray(p, plength);
# }
# }
# else
# {
# for (; i <= n - m; i++)
# {
# *(p+k) = a[i];
# printCombination(a+i, n - i, m - 1,k+1,p,plength);
# }
#
# }
# }
# void printAll(int*a, int length)
# {
#     int newlength = length + 1;
# int* p = (int*)malloc(sizeof(int) * newlength);
# *p = 0;
# for (int i = 0; i < length; i++)
#     *(p + i + 1) = *(a + i);
# for (int j = 1; j <=length; j++)
# {
#     int*pp= (int*)malloc(sizeof(int) * j);
# printCombination(p, newlength, j, 0,pp,j);
# printf("\n");
# }
# }
# int main()
# {
#     int a[] = {1,2,3,4,5,6,7,8,9 };
# printAll(a,9);
# }



