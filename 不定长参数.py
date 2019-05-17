#!/usr/bin/python
# -*- coding:utf-8 -*-
'''

概念：能处理比定义时更多的参数

'''
#加了星号（*）的变量存放所有未命名的变留参数，如果在函数调用时没有指定参数，他就是一个空元组
def func(name, *args):
    print(name)
    print(type(args))
    for x in args:
         print(x)
func("tom")



def mySum(*l):
    sum =0
    for i in l:
        sum +=i
    return sum

print(mySum(1,2,3,4))




def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))

func2(x=1,y=2,z=3)


