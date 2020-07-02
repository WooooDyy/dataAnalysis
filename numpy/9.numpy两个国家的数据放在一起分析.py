#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import numpy as np
from matplotlib import  pyplot as plt
us_file_path="../youtube_video_data/US_video_data_numbers.csv"
uk_file_path="../youtube_video_data/GB_video_data_numbers.csv"


#加载国家数据
tus=np.loadtxt(us_file_path,delimiter=",",dtype="int64")
tuk=np.loadtxt(uk_file_path,delimiter=",",dtype="int64")

#添加国家信息
#构造全为0的数据
zerosdata=np.zeros((tus.shape[0],1)).astype(int)#传入形状
onesdata=np.ones((tuk.shape[0],1)).astype(int)#传入形状

#分别添加一列全为0,1的数据
tus=np.hstack((tus,zerosdata))
tuk=np.hstack((tuk,onesdata))

#拼接两组数据
finaldata=np.vstack((tus,tuk))
print(finaldata)


