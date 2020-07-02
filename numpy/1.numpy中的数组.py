#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np
import random
# use numpy to create array
t1=np.array([1,2,3])
print(t1)
print(type(t1))

t2=np.array(range(10))
print(t2)


t3=np.arange(10)
print(t3)


print(t3.dtype)

t4=np.array(range(1,4),dtype=float)
t4=np.array(range(1,4),dtype="int8")
print(t4.dtype)
#modify type
t5=t4.astype("int64")

print(t4.dtype)

# numpy中的小数
t7=np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

t8=np.round(t7,2)
print(t8)

