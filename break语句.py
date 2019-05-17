#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
break语句:
作用：跳出for和while循环
注意：只能跳出距离最近的那一层循环
'''

for i in range(10):
    print(i)
    if i == 5:
        break


num = 1
while num <= 10:
    print(num)
    if num == 3:
        break
    num += 1
print(num)