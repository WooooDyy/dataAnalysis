#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np

us_file_path="../youtube_video_data/US_video_data_numbers.csv"
uk_file_path="../youtube_video_data/GB_video_data_numbers.csv"

t1=np.loadtxt(us_file_path,delimiter=",",dtype="int64",unpack=True)

print(t1)


print("-"*100)
t2=np.loadtxt(us_file_path,delimiter=",",dtype="int64",unpack=False)

print(t2)
# 转置的三种方法
# t2.transpose()
# t2.T
# t2.swapaxes()

