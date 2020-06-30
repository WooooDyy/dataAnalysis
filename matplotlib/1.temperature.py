#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from matplotlib import pyplot as plt

# 实例化一个fig，后台自动使用，后面都可以用，size是大小，dpi决定清晰度
fig=plt.figure(figsize=(20,8),dpi=80)

x = range(2,26,2)

y=[15,13,14.5,17,20,25,26,26,27,22,18,15]
#绘制
plt.plot(x,y)

#设置x周的刻度
# plt.xticks(x)
_xtick_labels=[i/2 for i in range(4,50)]
plt.xticks(_xtick_labels[::3])#取步长
plt.yticks(range(min(y) ,max(y)+1))

#保存到 本地
plt.savefig("./1.temperature.png")

#展示
plt.show()
