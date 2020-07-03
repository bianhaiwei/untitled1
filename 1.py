#!/usr/bin/python
# -*- coding:utf-8 -*-
#左移动两位
print(2 << 2)
#0000010
print (hello world)
print (hello k8s)
print (hello docker)
#右移动两位
print(13 >> 2)
#000001101
#000000011

#创建字符串
str1 = "abc"

#字符串运算

str2 = 'bsc'

str4 = 'dd'

str3 = str2 + str4

print(str3)

str11 = 'sunck is a good man'
print(str11[1])
#截取字符串
str12 = 'sunck is a good man'

str13 = str12[6:15]
print(str13)

str15 = 'sunck is a good man'
print('good '  not in str15)

#能被4整除但是不能被100整除，或 能被400整除

# year = int(input('年'))
#
# if  year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print('是闰年')
# else:
#     print('不是闰年')

num = 10
str16 = 'sunck is a good man'
print("num = %d \nstr16 = %s" % (num, str16))

print("tom \\ is")
print('tom is good  man')
print('''
good
nice

''')
# \t 制表符
print("sunck\tgood")
#如果字符串中有好多字符串都需要转译就需要多处\转译，python允许用 r
print(r"\\\t\\")

num1 = eval("123")
print(num1)
print(type(num1))
num2 = eval("12 - 3")
print(num2)

str16 = 'Sunck is a Good Man'

print(str16.lower())
print(str16.upper())

str17 = 'sunck is a good man'

print(str17.capitalize())
print(str17.title())

str18 = " tom is nice man"
#center(width[, fillchar])
#返回一个指定宽度的居中字符串，fillchar 为填充的字符串，默认空客填充
print(str18.center(40, "*"))
#返回一个指定宽度的左对齐字符串，fillchar 为填充的字符串，默认空客填充
print(str18.ljust(40,'*'))
#返回一个指定宽度的右对齐字符串，fillchar 为填充的字符串，默认空客填充
print(str18.rjust(40,'*'))
#find(str[,start] [,end])

str19 = " tom is nice man"
print(str19.index('nice'))

str20 ='a'
print(ord(str20))
str21 = 'abc'
print(len(str21))








