#!/usr/bin/python
# -*- coding:utf-8 -*-
#90 = 2x3x3x5
'''
num = int(input())
i =2
while  num != 1:
    if num % i == 0:
        print(i)
        num //= i
    else:
        i +=1

'''
str = input("输入字符串:")
str1 = str.strip()
index = 0
count = 0
# tom is a good man
while index < len(str1):
    while str1[index] != " ":
        index += 1
        if index == len(str1):
            break


    count += 1
    if index == len(str1):
        break
    while str[index] == " ":
        index += 1

print(count)

