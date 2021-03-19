# coding: utf-8
"""
    @author: zhangjk
    @file: draw_fib.py
    @date: 2020-02-28
    说明：xxxx
"""


import numpy as np
import pylab as plt

# 产生菲波那切数列
def fibo(n):
    f_0 = 0
    f_1 = 1
    fibo_list = np.array([f_0,f_1])
    for i in np.arange(n-2):
        fibo_num = f_0 + f_1
        fibo_list = np.append(fibo_list,fibo_num)
        f_0, f_1 = f_1, fibo_num
    return fibo_list

#找出各个圆心
def find_o_xy(f_list):
    import pylab as plt
    x_n, y_n = 0, 0         #起始圆心坐标
    o_x_array, o_y_array = np.array([x_n]), np.array([y_n])
    for n in np.arange(1,len(f_list)):
        #需要注意pyhton中数组计数是从0开始
        #第一项作为起始点已经给出
        y_n=y_n+np.mod(n+1,2)*f_list[n]*(-1)**(1+(np.mod(n+1,2)+n+1)/2)
        x_n=x_n+np.mod(n,2)*f_list[n]*(-1)**(1+(np.mod(n+1,2)+n+1)/2)
        o_x_array = np.append(o_x_array, x_n)
        o_y_array = np.append(o_y_array, y_n)
    return o_x_array, o_y_array

count = 5
f_list = fibo(count)
x0_array,y0_array = find_o_xy(f_list)
#------------------------头像4----------------------------
f_list_r = fibo(count+2)[2::]
start_angle, end_angle = np.pi, 1.5*np.pi
fig = plt.figure(num=1,facecolor='k',figsize=(10,10))

#增加坐标轴对象，显示box
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=True,aspect=1)

x_min, x_max, y_min, y_max = 0, 0, 0, 0
for n in np.arange(len(f_list_r)):
    #圆心坐标
    x0 = x0_array[n]
    y0 = y0_array[n]
    #得到对角顶点坐标
    x2 = x0+f_list_r[n]*(-1)**((np.mod(n+1,2)+n+1)/2)
    if n == 0:
        y2 = -1         #起始点特殊目前只想到这么整了
    else:
        y2 = y0+f_list_r[n]*(-1)**(1+(np.mod(n,2)+n)/2)
    #画出圆弧
    t=np.arange(start_angle,end_angle,0.001)
    circle_x = (f_list_r[n])*(np.sin(t))+x0_array[n]
    circle_y = (f_list_r[n])*(np.cos(t))+y0_array[n]
    start_angle += 0.5*np.pi
    end_angle += 0.5*np.pi
    #画图，在坐标轴上画图
    ax.plot(np.append(x0_array[n],np.append(circle_x,x0_array[n])),
            np.append(y0_array[n],np.append(circle_y,y0_array[n])),
            color='k',linewidth=5)

    ax.fill(np.append(circle_x,x0_array[n]),
            np.append(circle_y,y0_array[n]),
            facecolor='gold',
            alpha = 1)#f5bf03

#设置axes内的填充颜色
ax.patch.set_facecolor('k')

#调节坐标范围
x_min,x_max=8.5,-11.5
y_min,y_max=10,-10
mul_times = 1.5
ax.set_xlim(x_min*mul_times, x_max*mul_times)
ax.set_ylim(y_min*mul_times, y_max*mul_times)

#不显示坐标轴刻度以及刻度线
ax.tick_params(axis='both',labelsize=0,length=0)

#设置spine,即图形边框
ax.spines['top'].set_color('none')    #设置颜色
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')

#设置图片保存为png格式，有背景
plt.savefig('sdf.png',format = 'png',transparent=False,dpi=300)
