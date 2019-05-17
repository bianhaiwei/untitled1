#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
set:类似dict，是一组key的集合不存value

本质：无序和无重复的集合


'''

#创建
#创建set需要一个list或者list或者tuple或者dict作为输入集合
#重复元素在set中会自动被过滤

s1 = set([1,2,3,4,5,6])
print(type(s1))
print(s1)

s2 =set((1,1,3,4,5,2,3))
print(s2)
s3 = set({"tom":21,"jack":20})
print(s3)

#添加
s4 = set([1,2,3,4])
s4.add(6)
#s4.add([7,8,9])#set 的元素不能是列表，因为列表是可变的

print(s4)



#插入整个list，tuple，字符串，打碎插入
s5 = set([1,3,4,5,6,7])

s5.update([6,7,8])
s5.update((9,10))
s5.update("sunck")
print(s5)

#删除
s6 = set([1,2,3,4,5])
s6.remove(3)
print(s6)


#遍历
s7 = set([1,2,3,4,5])
for i in s7:
    print(i)


#set 没有索引



s8 = set([1,2,3])
s9 = set([2,3,4])
#交集
a1 = s8 & s9
print(a1)
a2 = s8 | s9
print(a2)
print(type(a2))