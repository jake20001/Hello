# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/10/3 16:42
# FileName : zfx
# Description : 
# --------------------------------


import turtle
turtle.reset()
turtle.begin_fill()
a= 60
turtle.fillcolor("red")
turtle.pencolor("blue")
turtle.pensize(10)

turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)

turtle.end_fill()

turtle.mainloop()