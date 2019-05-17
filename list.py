#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
创建列表
格式：列表名 = [列表选项1，列表选项2]
'''
list1 = []
'''
list2 = [18,20,19,21]
index = 0
sum = 0
while index <4:
    sum += list2[index]
    index += 1
    if index == 4:
        print("平均年龄%d" % (sum /4))
'''

#在末尾一次性追加另一个列表中的多个值
list2 =[1,2,3,4,5]
list2.extend([7,8,9])
print(list2)

#在下标除添加一个元素，不覆盖原数据，
list3 =[2,345,56,7,8]
list3.insert(2,200)
print(list3)
# remove 删除列表中的某个元素第一个匹配的元素
# clear 清除列表中的所有元素
# index 从列表中找出某个值第一个匹配的索引值
#count 查看元素在列表中出现的次数

'''
list4 = [1,2,3,4,3,4,3,5]
num = 0
all = list4.count(3)
while num < all:
    list4.remove(3)
    num += 1
print(list4)
'''
#倒叙
list5 = [1,2,3,4,5]
list5.reverse()
print(list5)

#升序
list6= [2,1,3,5,6]
list6.sort()
print(list6)

list7 = [1,2,3,4,5,6,]
list8 = list7.copy()
list8[1] = 200
print(list7)
print(list8)