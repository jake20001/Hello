# coding: utf-8
"""
    @author: zhangjk
    @file: drawSnake.py
    @date: 2020-02-07
    说明：xxxx
"""

import turtle  # 导入turtle库
pen: object = turtle.Pen()
pen.pensize(50)        # 画笔大小
pen.pencolor("purple")  # 画笔颜色
pen.setheading(-40)

pen.circle(40, 80)    # 参数表示半径
pen.circle(-40, 80)
pen.circle(40, 80)
pen.circle(-40, 80)
pen.setheading(0)
pen.forward(30)  #向前30
pen.circle(30, 180)
pen.dot(8, "white")    # 加点大小8，颜色白
pen.begin_fill()

turtle.done()