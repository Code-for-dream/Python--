#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/8 7:44
#!@Author: zyx
#!@File: .py
#数组的创建
import numpy as np
import random

t1 = np.array([1,2,3,4])
print(t1) #[1 2 3 4]
print(type(t1)) #该数组的类型  <class 'numpy.ndarray'>
print(t1.dtype) #该数组内元素的数据类型 int32 （32/64位）

t101 = np.array([1,2,3,4],dtype=float) #添加dtype属性，手动赋数据类型
print(t101) #[1. 2. 3. 4.]
print(t101.dtype) #float64

t102 = np.array([1,0,1,1,0],dtype=bool)
print(t102) #[ True False  True  True False]
print(t102.dtype) #bool
t103 = t102.astype("int8") #调整数据类型
print(t103) #[1 0 1 1 0]
print(t103.dtype) #int8

#arange生成的效果与array相似，可以快速的生成数组
t2 = np.array(range(10))
print(t2) #[0 1 2 3 4 5 6 7 8 9]
t3 = np.arange(10)
print(t3) #[0 1 2 3 4 5 6 7 8 9]
t4 = np.arange(1,10,2) #从1到10，步长为2
print(t4) #[1 3 5 7 9]

#numpy中取小数
t5 = np.array([random.random() for i in range(10)])
print(t5) #[0.43902813 0.3838124  0.57498559 0.83616761 0.71580552 0.3064713 0.47795043 0.17326671 0.38841184 0.7184412 ]
print(t5.dtype) #float64

#修改小数位
t6 = np.round(t5,2)
print(t6) #[0.64 0.72 0.73 0.63 0.52 0.53 0.75 0.84 0.48 0.11]
t7 = np.round([random.random()],3)
print(t7)  #[0.825]

