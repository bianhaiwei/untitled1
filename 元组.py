#!/usr/bin/python
# -*- coding:utf-8 -*-
#元组元素的访问

#格式：元组名[下标]

#元组中的元素不能变

#删除元组

tuple1 = (1,2,3)

#元组的操作
t1 = (1,2,3,4)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)

#元组的截取

#元组的方法

t5 = (1,2,3,4)

#len 返回元组中元素的个数

print(len(t5))

#max()
#min()

#将列表转成元组
list = [1,2,3,4]
t6 = tuple(list)
print(t6)

for i in (1,2,3,4):
    print(i)
