#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STSONG.TTF', size=10);

y=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x=range(11,31)

plt.figure(figsize=(20,8),dpi=80)


plt.plot(x,y)

_xtick_labels = ["{}岁".format(i) for i in range(11,31)]
plt.xticks(x,_xtick_labels,fontproperties=my_font)
plt.yticks(list(i/2 for i in range(0,15)))

#绘制网格
plt.grid(alpha=0.4)#alpha透明度

plt.show()
