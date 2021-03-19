# coding: utf-8
"""
    @author: zhangjk
    @file: str2excel.py
    @date: 2020-03-09
    说明：xxxx
"""
import turtle
from turtle import Turtle


class WuGui(object):

    def __init__(self):
        self.name = 'Gui'
        self.turtle = Turtle()

    def drawCase(self,stretch_wid=1, stretch_len=1, outline=1):
        self.turtle.setpos(0,0)
        self.turtle.resizemode("user")
        self.turtle.shape("turtle")
        self.turtle.shapesize(stretch_wid, stretch_len, outline)
        self.turtle.pencolor("blue")

    def running(self):
        turtle = self.turtle
        turtle.speed(6)
        turtle.color("blue","orange")
        turtle.pensize(2)
        turtle.setheading(turtle.towards(turtle))
        count = 1
        angle = -0.5
        fdistance = 3
        while True:  # turtle.distance(turtle) > 4:
            try:
                turtle.fd(fdistance)
                turtle.lt(count+angle)
                # if count % 5 == 0:
                #     turtle.bk(6)
                # turtle.setheading(turtle.towards(turtle))
                # tri.fd(4)
                # if count % 20 == 0:
                #     turtle.stamp()
                # tri.stamp()
                count += 1
                print(turtle.heading())
            except:
                exit(0)

    def show(self):
        turtle.mainloop()


def main():
    mWuGui = WuGui()
    mWuGui.drawCase(1,1)
    mWuGui.running()
    mWuGui.show()

if __name__ == '__main__':
    main()