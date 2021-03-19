# coding: utf-8
"""
    @author: zhangjk
    @file: num.py
    @date: 2020-02-03
    说明：xxxx
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

WIDTH = 100 * 4 * 2
HEIGHT = 100 * 4

image = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
# ,'white' 'red', 'green', 'blue',
colors = ['purple','gray']
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 32, encoding="unic")
d = []
def dx(a1,c1,b1,d1,n):
    for i in range(10):
        d.append({'x1':   a1, 'y1':   c1, 'x2':  b1, 'y2':  d1, 'number': n})
        a1 = a1+80
        b1 = b1+80
        n = n+1

for i in range(10):
    dx(1,1+i*40,80,40+i*40,1+10*i)
# dx(1,40,40,80,11)
# dx(1,40,40,80,11)

# d = [
#     {'x1':   1, 'y1':   1, 'x2':  40, 'y2':  40, 'number': 1},
#     {'x1':   41, 'y1':   1, 'x2':  80, 'y2':  40, 'number': 2},
#     {'x1':  81, 'y1':  1, 'x2':  120, 'y2':  40, 'number': 3},
#     {'x1':  121, 'y1':  1, 'x2': 160, 'y2': 40, 'number': 4},
#     {'x1':  81, 'y1':  81, 'x2': 120, 'y2': 120, 'number': 4}
# ]
for o in d:
    draw.rectangle(( o['x1'],  o['y1'], o['x2'],  o['y2']), colors[random.randint(0,len(colors)-1)], 'black')
    draw.text((o['x1'],  o['y1']), str(o['number']), 'white', font)

image.show()
# image.save('code.jpg', 'jpeg')