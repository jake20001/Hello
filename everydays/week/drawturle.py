# coding: utf-8
"""
    @author: zhangjk
    @file: drawturle.py
    @date: 2020-02-07
    说明：xxxx
"""

import turtle
turtle.setup(800,600)
turtle.speed(6)
turtle.colormode(255)
turtle.color((0,0,0),(60,100,30))
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()
turtle.pensize(2)
turtle.penup()
turtle.goto(190,-60)
turtle.pendown()
turtle.goto(-190,-60)
turtle.penup()
turtle.goto(190,60)
turtle.pendown()
turtle.goto(-190,60)
turtle.penup()
turtle.goto(60,190)
turtle.pendown()
turtle.goto(60,-190)
turtle.penup()
turtle.goto(-60,190)
turtle.pendown()
turtle.goto(-60,-190)
turtle.penup()
turtle.pensize(1)
turtle.goto(20,198)
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.color((0,0,0),(60,80,30))
turtle.begin_fill()
a=1
turtle.speed(0)
for i in range(120):
    if 0<=i<30 or 60<=i<=90:
        a=a+0.04
        turtle.lt(3)
        turtle.fd(a)
    else:
        a=a-0.04
        turtle.lt(3)
        turtle.fd(a)
turtle.penup()
turtle.end_fill()

turtle.color((0,0,0),(255,255,255))
turtle.goto(11,240)
turtle.begin_fill()
turtle.pendown()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.end_fill()
turtle.color((0,0,0),(255,255,255))
turtle.goto(-11,240)
turtle.begin_fill()
turtle.pendown()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.color((0,0,0),(0,0,0))
turtle.goto(10,240)
turtle.begin_fill()
turtle.pendown()
turtle.circle(3)
turtle.end_fill()
turtle.penup()
turtle.end_fill()
turtle.color((0,0,0),(0,0,0))
turtle.goto(-10,240)
turtle.begin_fill()
turtle.pendown()
turtle.circle(3)
turtle.end_fill()
turtle.penup()
turtle.color((0,0,0),(60,80,30))
turtle.goto(-120,150)
turtle.pendown()
turtle.seth(30)
turtle.begin_fill()
a=0.3
for i in range(120):
    if 0<=i<30 or 60<=i<=90:
        a=a+0.06
        turtle.lt(3)
        turtle.fd(a)
    else:
        a=a-0.06
        turtle.lt(3)
        turtle.fd(a)
turtle.end_fill()
turtle.penup()
turtle.goto(120,150)
turtle.pendown()
turtle.seth(-30)
a=0.3
turtle.begin_fill()
for i in range(120):
    if 0<=i<30 or 60<=i<=90:
        a=a+0.06
        turtle.lt(3)
        turtle.fd(a)
    else:
        a=a-0.06
        turtle.lt(3)
        turtle.fd(a)
turtle.penup()
turtle.end_fill()
turtle.goto(-120,-160)
turtle.pendown()
turtle.seth(-210)
turtle.begin_fill()
a=0.5
for i in range(120):
    if 0<=i<30 or 60<=i<=90:
        a=a+0.03
        turtle.lt(3)
        turtle.fd(a)
    else:
        a=a-0.03
        turtle.lt(3)
        turtle.fd(a)
turtle.penup()
turtle.end_fill()
turtle.goto(120,-160)
turtle.pendown()
turtle.seth(210)
turtle.begin_fill()
a=0.5
for i in range(120):
    if 0<=i<30 or 60<=i<=90:
        a=a+0.03
        turtle.lt(3)
        turtle.fd(a)
    else:
        a=a-0.03
        turtle.lt(3)
        turtle.fd(a)
turtle.end_fill()
turtle.penup()
turtle.goto(0,-200)
turtle.seth(0)
turtle.pendown()

turtle.begin_fill()
turtle.fd(10)
turtle.seth(-105)
turtle.fd(30)
turtle.seth(105)
turtle.fd(30)
turtle.seth(0)
turtle.fd(10)
turtle.end_fill()
turtle.hideturtle()
turtle.mainloop()