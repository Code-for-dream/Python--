#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/5 19:31
#!@Author: zyx
#!@File: .py
from matplotlib import pyplot as plt
from matplotlib import font_manager

#设置字体
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

#设置数据
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60] #组距
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

#绘制图形
plt.bar(range(len(quantity)),quantity,width=1)

#设置x轴刻度
x_ = [i-0.5 for i in range(13)]
_x_labels = interval+[150]
plt.xticks(x_,_x_labels)

#添加信息
plt.xlabel("所花时间(分钟)",fontproperties=my_font)
plt.ylabel("数量（人）",fontproperties=my_font)
plt.title("2004年美国人花费在上班途中的时间分布图",fontproperties=my_font)

#设置网格
plt.grid(True,linestyle="-.",alpha=0.3)

#展示
plt.show()
