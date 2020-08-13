#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/4/19 19:53
#!@Author: zyx
#!@File: .py
#如果列表a便是10点到12点的每一分钟的气温，绘制折线图
# a=[random.randint(20,35)for i in range(120)]
#解决中文不显示问题
#fc-list  -->查看支持的字体
#fc-list :lang=zh -->查看支持的中文（冒号前有空格）

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import  font_manager

#1.windows\linux设置字体
#font = {'family' : 'MicroSoft YaHei',
#        'weight' : 'bold',
#        'size'   : 'larger'}
#matplotlib.rc("font",**font) #查看源码ctrl+b

#2.另一种设置字体方式
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

#定义x、y轴
x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

#修改大小尺寸
plt.figure(figsize=(20,8),dpi=80)

#绘制
plt.plot(x,y)

#调整x轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]

#取适当步长，将数字与x轴字符串对应，使得数据长度保持一致
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font) #将x轴字符串旋转45度

#添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位（°c）",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)

#显示图示
plt.show()