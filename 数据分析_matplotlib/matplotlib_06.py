#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/4/29 15:31
#!@Author: zyx
#!@File: .py
#假设知道几部电影在某三天的上映量，展示出电影本身票房以及同其他几部电影的票房对比
from matplotlib import pyplot as plt
from matplotlib import font_manager

#设置字体
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

#设置坐标轴
x = ["猩球崛起3:终极之战","敦刻尔克","蜘蛛侠:英雄归来","战狼2"]
y_20 = [15746,312,4497,319]
y_21 = [12357,156,2045,168]
y_22 = [2358,399,2358,362]

bar_width = 0.2
x_20 = list(range(len(x)))
x_21 = [i+bar_width for i in x_20]
x_22 = [i+bar_width*2 for i in x_20]

#设置大小
plt.figure(figsize=(20,8),dpi=80)

#绘制
plt.bar(range(len(x)),y_20,width=bar_width,label="8月20日")
plt.bar(x_21,y_21,width=bar_width,label="8月21日")
plt.bar(x_22,y_22,width=bar_width,label="8月22日")

#设置坐标信息
plt.xticks(x_21,x,fontproperties=my_font)
#添加描述信息
plt.xlabel("电影名称",fontproperties=my_font)
plt.ylabel("当日票房/万元",fontproperties=my_font)
plt.title("8月份某3天4部电影各自票房变化",fontproperties=my_font)


#绘制图例
plt.legend(prop=my_font)

#展示
plt.show()
