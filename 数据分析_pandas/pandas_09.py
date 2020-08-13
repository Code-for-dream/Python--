#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/6/14 9:57
#!@Author: zyx
#!@File: .py
#使用matplotlib呈现出店铺总数排名前十的国家
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

#设置字体
#设置字体
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\STXINGKA.TTF",size=18)

#准备数据
file_path = "starbucks/directory.csv"
df = pd.read_csv(file_path)

data = df.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]

x = data.index
y = data.values

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

#绘图
plt.bar(range(len(x)),y)
plt.xticks(range(len(x)),x)

#添加信息
plt.xlabel("国家",fontproperties=my_font)
plt.ylabel("该国星巴克店铺数",fontproperties=my_font)
plt.title("星巴克店铺总数排名前十的国家",fontproperties=my_font)

#展示
plt.show()
