#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np
import random

t1 = np.arange(12)
print(t1.shape)
t2=np.array([[1,2,3],
            [4,5,6]])
print(t2.shape)

t3=np.array([
                [
                    [1,2,3],
                    [4,5,6]
                ],
                [
                    [7,8,9],
                    [4,5,6]
                ]
            ] )



print(t3.shape)

t4=np.array([0,1,2,3,4,5,6,7,8,9,10,11])
t4=t4.reshape(3,4)
print(t4.shape)

t5=np.arange(24).reshape((2,3,4))
print(t5)

# t6=t5.reshape(4,6)
# print(t6)
t6=t5.reshape((t5.shape[0]*t5.shape[1]*t5.shape[2],))
print(t6)
#数据变成一维
t6=t5.flatten()

print(t6)

#广播性质，全部加
t7t=t5+2

t6=np.arange(100,124).reshape((2,3,4))
t7=t5+t6
