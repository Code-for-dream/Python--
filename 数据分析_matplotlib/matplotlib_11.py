#!/usr/bin/env python
#!-*-coding:utf-8 -*-
#!@Time:2020/6/24 16:13
#!@Author: zyx
#!@File: .py
#love爱心
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))