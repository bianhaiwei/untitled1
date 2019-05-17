#!/usr/bin/python
# -*- coding:utf-8 -*-

def outer(func):
    def inner(*args,**kwargs):
        #添加修改的功能
        print("*****")
        func(*args,**kwargs)
    return inner
@outer
def say(name,age):
    print("%s years old is %d" %(name,age))#函数的参数理论上是无限制的，但实际上最好不要超过6，7个
    return "aaa"
say("tom", 21)
