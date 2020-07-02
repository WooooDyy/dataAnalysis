#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import numpy as np



def fill_ndarray(t1):
    for i in range(t1.shape[1]):
        temp_col=t1[:,i] #当前列
        nan_num= np.count_nonzero(temp_col!=temp_col)
        if nan_num !=0:#不为0 说明这一列中有nan
            temp_notNanCol = temp_col[temp_col==temp_col] #当前一列部不为nan的array
            print(np.isnan(temp_col))
            print(temp_col[np.isnan(temp_col)])
            temp_col[np.isnan(temp_col)] = temp_notNanCol.mean() #选中当前为nan的位置，把值赋值为不为nan的均值
    return t1

if __name__=='__main__':
    t1=np.arange(12).reshape((3,4)).astype("float")

    t1[1,2:]=np.nan
    t1=fill_ndarray(t1)
    print(t1)