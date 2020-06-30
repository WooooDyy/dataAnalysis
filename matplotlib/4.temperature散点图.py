#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STSONG.TTF', size=10);

y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3=range(1,32)
x_10=range(51,82)

x= range(1,32)

plt.figure(figsize=(15,8),dpi=80)

plt.scatter(x_3,y_3,label="3月")
plt.scatter(x_10,y_10,label="10月")


#调整x轴
_x=list(x_3)+list(x_10)
_xtick_labels=["三月{}日".format(i) for i in x_3]
_xtick_labels+=["十月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)
#DESCRIPTION
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.title("三月和十月份降水量",fontproperties=my_font)


plt.legend(loc=1,prop=my_font)

plt.show()