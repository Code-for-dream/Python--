#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/4/19 16:29
#!@Author: zyx
#!@File: .py

from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)

#设置x轴
#plt.xticks(range(2,25,0.5))
#_xtick_labels=[i/2 for i in range(4,49)] 通过传递步长参数设置步长
#plt.xticks(_xtick_labels)
_xtick_labels=[i/2 for i in range(4,49)]
plt.xticks(_xtick_labels[::3]) #取消步长，每隔3个步长取一个刻度
#设置y轴
plt.yticks(range(min(y),max(y)+1)) #y值分布于y(min)、y(max)之间，yticks方法最后取不到

#绘图
plt.plot(x,y)

#保存图片
#plt.savefig("./t1.png")

#展示图形
plt.show()

