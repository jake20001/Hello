# coding : utf-8
'''
    @author :  zhang.jianke
    @project:  WorkSpaceDemo
    @file   :  bike.py
    @date   :  2020-04-06

    假设两地相距20Miles；
    2个人自行车10Mile/H相向而行；一个苍蝇以15Mile/H来回在他们之间飞行（遇到其中一个人后返回）；问当他们相遇时，
    苍蝇飞了多少Miles？
'''


class Distance(object):

    def __init__(self,distance):
        self.distance = distance

    def cost(self,n,q):
        s = 0
        for i in range(n):
            x = 1
            for k in range(i):
                x = q*x
            s = s + x
        return s


def main():
    mDistance = Distance(20)
    print(mDistance.cost(1000,0.2))


if __name__ == '__main__':
    main()