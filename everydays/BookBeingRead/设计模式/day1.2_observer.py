# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2021/1/21 19:43
# FileName : day1.2_observer
# Description : 
# --------------------------------


class StealerParent(object):

    def __init__(self):
        self.polices = []

    def add(self,police):
        if police not in self.polices:
            self.polices.append(police)

    def warning(self):
        for police in self.polices:
            police.notify(self)


class Stealer(StealerParent):

    def __init__(self):
        StealerParent.__init__(self)
        self.name = "C Stealer"

    def stealing(self):
        self.warning()


class PoliceA(object):

    def __init__(self):
        self.name = "A Sir"

    def notify(self,stealer):
        print(self.name,"catching ",stealer.name)


class PoliceB(PoliceA):

    def __init__(self):
        PoliceA.__init__(self)
        self.name = "B Sir"


def main():
    mStealer = Stealer()
    mPoliceA = PoliceA()
    mStealer.add(mPoliceA)
    mStealer.stealing()

    mPoliceB = PoliceB()
    mStealer.add(mPoliceB)
    mStealer.stealing()


if __name__ == '__main__':
    main()