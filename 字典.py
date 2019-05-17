#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
概述
使用键值（key-value）对存储，具有极快的查找

#字典时无序的


key 的特性
1.字典中的key必须唯一
2. key必须要是不可变的对象
3 字符串，整数都是不可变的，可以作为key
4 list 是可变的，不能作为key



思考：保存对为学生的姓名与成绩



使用字典，学生姓名为key ，学生成绩作为值


'''


dict1 = {"tom":60,"lilei":70}

#元素的访问
#获取：字典名[key]

print(dict1["tom"])
print(dict1["lilei"])

print(dict1.get("sunck"))

#添加
dict1["hanmeimei"] = 99

print(dict1)

#删除

dict1.pop("tom")
print(dict1)


#遍历

for key in dict1:
    print(key,dict1[key])

print(dict1.values())
for value in dict1.values():
    print(value)


for k ,v in dict1.items():
    print(k,v)



for i ,v2 in enumerate(dict1):
    print(i,v2)




#和list比较
#1 查找和插入的速度极快，不会随着key-value的增加而变慢
#需要占用大量的内存，内存浪费多

#list
#随着数据的增加查找的速度变慢
#占用内存少















