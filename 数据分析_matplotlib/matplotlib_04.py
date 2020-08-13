#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/4/25 11:54
#!@Author: zyx
#!@File: .py
#已知某地3、10月份的气温，绘制散点图
from matplotlib import pyplot as plt
from matplotlib import font_manager

#设置字体
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

#设置坐标
x_3 = range(1,32)
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,23,20]
x_10 = range(41,72)
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

#设置大小
plt.figure(figsize=(20,8),dpi=80)

#绘图
plt.scatter(x_3,y_3,label="3月份")
plt.scatter(x_10,y_10,label="10月份")

#调整刻度
_x=list(x_3)+list(x_10)
_xtick_labels=["3月{}日".format(i) for i in x_3]
_xtick_labels+=["10月{}日".format(i-40) for i in x_10]
plt.xticks(_x,_xtick_labels,rotation=45,fontproperties=my_font)
plt.yticks(range(0,31))

#添加描述信息
plt.xlabel("月份",fontproperties=my_font)
plt.ylabel("气温°C",fontproperties=my_font)
plt.title("某地3月和10月的气温散点图",fontproperties=my_font)

#添加图例
plt.legend(prop=my_font)
#绘制网格,并设置透明度
plt.grid(alpha=0.3)

#显示
plt.show()