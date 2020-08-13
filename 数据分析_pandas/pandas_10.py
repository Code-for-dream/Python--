#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/6/14 10:14
#!@Author: zyx
#!@File: .py
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

#设置字体
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\STXINGKA.TTF",size=18)

#准备数据
file_path = "starbucks/directory.csv"
df = pd.read_csv(file_path)
df = df[df["Country"]=="CN"]

data = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:25]

x = data.index
y = data.values

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

#绘图
plt.barh(range(len(x)),y,height=0.3)
plt.yticks(range(len(x)),x,fontproperties=my_font)

#添加信息
plt.ylabel("城市",fontproperties=my_font)
plt.xlabel("该城市星巴克店铺数",fontproperties=my_font)
plt.title("中国星巴数排名前25的城市克店铺总数",fontproperties=my_font)

#绘制网格
plt.grid()

#展示
plt.show()
