# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/1/21 10:15
# FileName : day1.1_server
# Description : 组合式观察者
# --------------------------------

# 小偷组织
class StealerTeam(object):

    def __init__(self,name):
        self.name = name
        self.observers = []

    # 监控的人
    def add(self,observer):
        if observer not in self.observers:
            self.observers.append(observer)
        print("add",self.observers)

    # 发出通知
    def notify(self):
        print("notify",self.observers)
        for obsever in self.observers:
            obsever.send_warning()


# 小偷个体
class Stealer(object):

    def __init__(self,name,house):
        self.name = name
        self.house = house

    def steal(self,thing):
        print("%s steal %s"%(self.name,thing))
        print(self.house.observers)
        self.house.notify()



# 警察组织
class PeliceA(object):

    def __init__(self,name):
        self.name = name

    def send_warning(self):
        print("AAAAA",self.name)

class PeliceB(object):

    def __init__(self,name):
        self.name = name

    def send_warning(self):
        print("BBBBB",self.name)


def main():
    mStealerTeam = StealerTeam("ST")

    mStealer = Stealer("STAAAAAA",mStealerTeam)
    mPeliceA = PeliceA("xxxxxAAAA")
    mStealerTeam.add(mPeliceA)

    mStealer.steal("Bread")

    mPeliceB = PeliceB("xxxBBBB")
    mStealerTeam.add(mPeliceB)

    mStealer.steal('Milk')


if __name__ == '__main__':
    main()





