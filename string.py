#!/usr/bin/python
# -*- coding:utf-8 -*-

#split(str= "")

#以str为分隔符截取字符串，指定num，则仅截取num个字符串


str1 = "sunck**is****good*man"
list1 = str1.split("*")
print(list1)
c = 0
for s in list1:
    if len(s)> 0:
        c += 1
print(c)


#splitlines([keepends]) 按照（'\r','\r\n', '\n'）分隔,返回
#keepends == Ture 会保留换行符,默认为False
str2  = '''
sunck is a good man 
sunck is a nice man
sunck is a handsomeman
'''
print(str2.splitlines())

#join(seq) 以指定的字符串分隔符吗，将seq中的所有元素组合合成一个字符串
list2 = ['sunck' ,'is' ,'a', 'good', 'man']

str3 = ' '.join(list2)
print(str3)

#max() min

str4 = "sunck is good man "
print(max(str4))


#replace(oldstr,newstr,count )
#用newstr替换oldstr，默认是全部替换

str5 = "sunck is good man"

str6 = str5.replace("good","nice",1)

print(str6)
print(str5)

#创建一个字符串映射表
t7 = str.maketrans("ac","57")
str7 = "sunck is a good  good man"
str8 = str7.translate(t7)
print(str8)

#编码
#encode(encoding="utf-8",errors="strict")
str9 = "sunck is good man 你好"
data1 = str9.encode("utf-8", "ignore")


#ignore忽略错误
print(data1)

#解码  注意：要与编码时的格式一致
str10 = data1.decode("gbk","ignore")
print(str10)


#isalpha()
#如果字符串中至少有一个字符且所有的字符串都是字母返回Ture否则返回False

str11 = "sunck is a good man"
print(str11.isalpha())

#isalnum
#如果字符串中至少有一个字符且所有的字符串都是字母或数字返回Ture否则返回False
str12 = "adc123"
print(str12.isalnum())

#isupper
# 如果字符串中至少有一个英文字符，且所有英文字符都是大写的，返回Ture，后则返回False
#islower
 # 如果字符串中至少有一个英文字符，且所有英文字符都是小写写的，返回Ture，后则返回False
#istitle
#如果字符串是标题化全是大写的返回ture，否则返回False
print("Sunck Is".istitle())

#isdigit()
# 如果字符串中只包含数字返回ture，否则返回false
print("123".isdigit())
#isspace()
#如果字符串中只包含空格符的返回Ture，否则返回false