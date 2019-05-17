#!/usr/bin/python
# -*- coding:utf-8 -*-
#list ----> set
l1 = [1,2,3,4,5,6]

s1 = set(l1)
print(s1)


#tuple ---> set

t1 = (1,2,3,4,5)
s2 = set(t1)
print(s2)



#dict ---> list

d1 = {"tom":21,"jack":20}

s3 = set(d1)
print(s3)

#set ---> list

set1 = {1,2,3,4,5,6}
list1 = list(set1)
print(list1)

list2 = [1,2,3,3,4,5,5]

set2 = set(list2)
list3 = list(set2)
print(list3)
