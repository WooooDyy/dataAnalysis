#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STSONG.TTF', size=10);

y=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x=range(11,31)
y_2=[0,1,5,3,1,2,3,4,2,3,3,2,2,2,2,1,4,5,2,1]


plt.figure(figsize=(20,8),dpi=80)


plt.plot(x,y,label="自己",color="orange",linestyle=":",linewidth=2)#color可以输入十六进制
plt.plot(x,y_2,label="同桌",color="cyan",linestyle="--")#两张折叠图

_xtick_labels = ["{}岁".format(i) for i in range(11,31)]
plt.xticks(x,_xtick_labels,fontproperties=my_font)
plt.yticks(range(0,9))

#绘制网格
plt.grid(alpha=0.4,linestyle=":")#alpha透明度

plt.legend(prop=my_font,loc=2)#图例 只有这里是prop 其他都是properties

plt.show()
