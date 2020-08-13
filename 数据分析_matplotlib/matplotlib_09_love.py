#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/5/11 19:49
#!@Author: zyx
#!@File: .py
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import font_manager

#设置字体
my_font=font_manager.FontProperties(fname="C:\Windows\Fonts\STXINGKA.TTF",size=12)

def plot_love(numbers):
 for k in range(numbers):
  time.sleep(0.05)

  def f(x, love=50):
   y = x ** (2 / 3) + 0.9 * np.sqrt(3.3 - x ** 2) * np.sin(love * np.pi * x)
   return y

  x = np.linspace(0, 2, 1500)
  y = [f(i, k) for i in x]

  plt.plot(x, y, color='red', linewidth=5)
  plt.plot(-x, y, color='red', linewidth=5)
  plt.xlim(-2, 2)

  plt.title("我想说 \t 我会爱你多一点点 \t 一直就在你的耳边",fontproperties=my_font)
  plt.xlabel("相信我会爱你永远不变",fontproperties=my_font)

  plt.show()


plot_love(150)


