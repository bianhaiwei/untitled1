#!/usr/bin/python
# -*- coding:utf-8 -*-

year = int(input('输入年：'))

if  year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('是闰年')
else:
    print('不是闰年')