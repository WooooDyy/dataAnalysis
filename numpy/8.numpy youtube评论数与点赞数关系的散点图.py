#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np
from matplotlib import  pyplot as plt
us_file_path="../youtube_video_data/US_video_data_numbers.csv"
uk_file_path="../youtube_video_data/GB_video_data_numbers.csv"


print("-"*100)
tuk=np.loadtxt(uk_file_path,delimiter=",",dtype="int64")
#选择喜欢数比五十万小的数据
tuk = tuk[tuk[:, 1] <= 500000]

tUkComent=tuk[:,-1]
tUkLike=tuk[:,1]

plt.figure(figsize=(20,8),dpi=80)

plt.scatter(tUkLike,tUkComent)

plt.show()