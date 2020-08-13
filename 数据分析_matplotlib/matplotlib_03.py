#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/4/24 15:53
#!@Author: zyx
#!@File: .py
#你与朋友从11到30岁交的朋友数，并比较,绘制折线图
from matplotlib import pyplot as plt
from matplotlib import font_manager

#设置字体
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

#定义坐标轴
x = range(11,31)
y_1 = [2,3,3,4,6,5,6,5,8,5,4,6,4,4,4,4,4,3,3,3]
y_2 = [1,4,5,5,6,4,5,5,4,7,6,5,3,2,2,6,1,2,6,4]

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

#绘制
plt.plot(x,y_1,label="自己",color="purple",linestyle='-.')
plt.plot(x,y_2,label="朋友",color="cyan",linestyle='--')

#绘制x\y轴刻度,添加描述信息
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,fontproperties=my_font)
plt.yticks(range(0,10))
plt.xlabel("年龄",fontproperties=my_font)
plt.ylabel("每年交到的新朋友数",fontproperties=my_font)
plt.title("与朋友每年新交到朋友数量对比图",fontproperties=my_font)

#添加图例
plt.legend(prop=my_font,loc="upper left")

#绘制网格,并设置透明度
plt.grid(alpha=0.3)

#展示
plt.show()
