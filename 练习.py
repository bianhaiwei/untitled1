#!/usr/bin/python
# -*- coding:utf-8 -*-

w = input()
d = {}  #word : 次数
str1= "sunck is a nice man sunck is a good man sunck is a good man" \
      "sunck is a good man sunck is a good man"

l1 = str1.split()
print(l1)

for i in l1:
    c =d.get(i)
    if c == None:
        d[i] = 1
    else:
        d[i] +=1

print(d[w])

'''
1 一空格切割字符串
2 循环处理列表中的每个元素
3 以元素当做key去一个字典中提取数据
4 如果没有提取到，就以该元素作为key，1作为value存进字典
5 如果提取到，将对应的key的value修改 。值加1
6 根据输入的字符串当做key再去字典中取值         

'''





