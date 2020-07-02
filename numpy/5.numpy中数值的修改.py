#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import numpy as np

us_file_path="../youtube_video_data/US_video_data_numbers.csv"
uk_file_path="../youtube_video_data/GB_video_data_numbers.csv"


print("-"*100)
t2=np.loadtxt(us_file_path,delimiter=",",dtype="int64",unpack=False)

print(t2)
print("-"*100)
#大于10的值变成三
t2[t2>10]=3
print("-"*100)
print(t2)
#三元操作符小于10的变成0,其他变成10
t2=np.where(t2<10,0,10)
print("-"*100)

# 小于10变成10,大于18变成18
t2=t2.clip(10,18)
print(t2)
print("-"*100)
print(t2.shape)

#axis=0 逐列计算
s=np.sum(t2,axis=0)
print(s)
print("-"*100)
