#!/usr/bin/python
# -*- coding:utf-8 -*-

def outer(func):
    def inner(age):
        if age <0:
            age =0
        func(age)
    return inner
#使用@符号讲装饰器应用到函数
@outer  #

def say(age):
    print("tom is %d years old" %(age))

say(21)

say(-10)