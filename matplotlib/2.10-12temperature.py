#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# #设置字体 中文 Windows&linux
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 12}
# matplotlib.rc("font",**font)
my_font = font_manager.FontProperties(fname=r'C:\Windows\Fonts\STSONG.TTF', size=10);


x=range(0,120)
y=[random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#调整x轴刻度
_x=list(x)
print(_x)
_xtick_labels=["十点{}分".format(i) for i in range(60)]
_xtick_labels+=["十一点{}分".format(i) for i in range(60)]
#取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(_x[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)#数值型数字对应到字符串上面。 rotation 旋转


#添加描述信息
plt.xlabel("时间",fontproperties = my_font)
plt.ylabel("温度 单位（℃）",fontproperties = my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties = my_font)
plt.show()