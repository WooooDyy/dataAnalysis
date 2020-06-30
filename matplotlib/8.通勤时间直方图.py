#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from matplotlib import pyplot as plt
import random
import matplotlib
import math
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STSONG.TTF', size=10);

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

#没有经过统计,无法使用hist方法,所以绘制条形图来代替直方图

plt.figure(figsize=(20,8),dpi=80)

#很关键,调整直方图
for i in range(len(interval)):
    interval[i] = interval[i]+width[i]/2

plt.bar(interval,quantity,width=width)

# _x=[i-0.5 for i in range(13)]
# _xticik_labels=interval+[150]
# plt.xticks(_x,_xticik_labels)
# _x=[i+2.5 for i in interval]

_x=range(0,155,5)
plt.xticks(_x)
plt.show()

