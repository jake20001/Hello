"""
绘制小猪佩奇
"""
import turtle
from turtle import Turtle

tp = Turtle()

def nose(x,y):

    """画鼻子"""
    tp.penup()
    # 将海龟移动到指定的坐标
    tp.goto(x,y)
    tp.pendown()
    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    tp.setheading(-30)
    tp.begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i <90:
            a = a + 0.08
            # 向左转3度
            tp.left(3)
            # 向前走
            tp.forward(a)
        else:
            a = a - 0.08
            tp.left(3)
            tp.forward(a)
    tp.end_fill()
    tp.penup()
    tp.setheading(90)
    tp.forward(25)
    tp.setheading(0)
    tp.forward(10)
    tp.pendown()
    # 设置画笔的颜色(红, 绿, 蓝)
    tp.pencolor(255, 155, 192)
    tp.setheading(10)
    tp.begin_fill()
    tp.circle(5)
    tp.color(160, 82, 45)
    tp.end_fill()
    tp.penup()
    tp.setheading(0)
    tp.forward(20)
    tp.pendown()
    tp.pencolor(255, 155, 192)
    tp.setheading(10)
    tp.begin_fill()
    tp.circle(5)
    tp.color(160, 82, 45)
    tp.end_fill()


def head(x, y):
    """画头"""
    tp.color((255, 155, 192), "pink")
    tp.penup()
    tp.goto(x,y)
    tp.setheading(0)
    tp.pendown()
    tp.begin_fill()
    tp.setheading(180)
    tp.circle(300, -30)
    tp.circle(100, -60)
    tp.circle(80, -100)
    tp.circle(150, -20)
    tp.circle(60, -95)
    tp.setheading(161)
    tp.circle(-300, 15)
    tp.penup()
    tp.goto(-100, 100)
    tp.pendown()
    tp.setheading(-30)
    a = 0.4
    for i in range(60):
        if 0<= i < 30 or 60 <= i < 90:
            a = a + 0.08
            tp.lt(3) #向左转3度
            tp.fd(a) #向前走a的步长
        else:
            a = a - 0.08
            tp.lt(3)
            tp.fd(a)
    tp.end_fill()


def ears(x,y):
    """画耳朵"""
    tp.color((255, 155, 192), "pink")
    tp.penup()
    tp.goto(x, y)
    tp.pendown()
    tp.begin_fill()
    tp.setheading(100)
    tp.circle(-50, 50)
    tp.circle(-10, 120)
    tp.circle(-50, 54)
    tp.end_fill()
    tp.penup()
    tp.setheading(90)
    tp.forward(-12)
    tp.setheading(0)
    tp.forward(30)
    tp.pendown()
    tp.begin_fill()
    tp.setheading(100)
    tp.circle(-50, 50)
    tp.circle(-10, 120)
    tp.circle(-50, 56)
    tp.end_fill()


def eyes(x,y):
    """画眼睛"""
    tp.color((255, 155, 192), "white")
    tp.penup()
    tp.setheading(90)
    tp.forward(-20)
    tp.setheading(0)
    tp.forward(-95)
    tp.pendown()
    tp.begin_fill()
    tp.circle(15)
    tp.end_fill()
    tp.color("black")
    tp.penup()
    tp.setheading(90)
    tp.forward(12)
    tp.setheading(0)
    tp.forward(-3)
    tp.pendown()
    tp.begin_fill()
    tp.circle(3)
    tp.end_fill()
    tp.color((255, 155, 192), "white")
    tp.penup()
    tp.seth(90)
    tp.forward(-25)
    tp.seth(0)
    tp.forward(40)
    tp.pendown()
    tp.begin_fill()
    tp.circle(15)
    tp.end_fill()
    tp.color("black")
    tp.penup()
    tp.setheading(90)
    tp.forward(12)
    tp.setheading(0)
    tp.forward(-3)
    tp.pendown()
    tp.begin_fill()
    tp.circle(3)
    tp.end_fill()


def cheek(x,y):
    """画脸颊"""
    tp.color((255, 155, 192))
    tp.penup()
    tp.goto(x,y)
    tp.pendown()
    tp.setheading(0)
    tp.begin_fill()
    tp.circle(30)
    tp.end_fill()


def mouth(x,y):
    """画嘴巴"""
    tp.color(239, 69, 19)
    tp.penup()
    tp.goto(x, y)
    tp.pendown()
    tp.setheading(-80)
    tp.circle(30, 40)
    tp.circle(40, 80)


def setting():
    """设置参数"""
    tp.pensize(4)
    # 隐藏海龟
    tp.hideturtle()
    tp.screen.colormode(255)
    tp.color((255, 155, 192), "pink")
    tp.screen.setup(840, 500)
    tp.speed(10)


def main():
    """主函数"""
    setting() 
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    turtle.done()


if __name__ == '__main__':
    main()
