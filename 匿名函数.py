#!/usr/bin/python
# -*- coding:utf-8 -*-
'''

概念：不使用def这样的语句函数，使用lambda来创建匿名函数



特点：
1 lambda 是一个表达式，函数体比def简单
2 lambda 的主体是一个表达式。而不是代码块，仅仅只能在lambda表达式中封装简单的逻辑
3 lambd 函数有自己的命名空间，且不能访问自由参数列表之外的或则全局命名空间的参数



格式：lambda 参数1，参数2，...参数n：expression(表达式)

'''

sum =lambda num1,num2:num1+num2
print(sum(1,2))