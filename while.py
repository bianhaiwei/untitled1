#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
while 语句：

格式
while 表达式：
    语句

逻辑：当程序执行到while语句时，首先计算“表达式”的值，如果“表达式”的值为假，那么结束整个while语句。如果
“表达式”的值为真，则执行“语句”，执行完“语句”在执行“表达式”的值，如果“表达式”的值为假，那么结束整个
while循环。如果“表达式”的值为真，则执行“语句”，执行完“语句”再去计算“表达式”的值，如此循环往复，直到
表达式的值为假才停止。
'''
'''
num = 1
while num <= 5:
    print(num)
    num += 1

'''

sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1

print("sum = %d" % sum)

str = 'tom is good man'
index = 0
while index < len(str):
    print("str[%d] = %s" % (index,str[index]))
    index += 1


i=5
while i>0:
    print("Hello world")
    i -=1




