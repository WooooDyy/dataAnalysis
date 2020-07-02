#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np

us_file_path="../youtube_video_data/US_video_data_numbers.csv"
uk_file_path="../youtube_video_data/GB_video_data_numbers.csv"


print("-"*100)
t2=np.loadtxt(us_file_path,delimiter=",",dtype="int64",unpack=False)

print(t2)
print("-"*100)

# 取行
print(t2[2])
print("-"*100)

# 取连续的多行
print(t2[2:])
print("-"*100)

# 取不连续的多行
print(t2[[2,8,10]])
print("-"*100)

#取列
print(t2[:,2])
print("-"*100)

print(t2[[1,2,3],2])
print("-"*100)

# 连续多列
print(t2[:,2:])
print("-"*100)

# 不连续多列
print(t2[:,[0,2]])
print("-"*100)

#取第三行第四列
print(t2[2,3])
print("-"*100)

#多行多列
print(t2[2:4,1:3])

#取多个不相邻的点,结果是(0,0),(2,1)
c=t2[[0,2],[0,1]]

