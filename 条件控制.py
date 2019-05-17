#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
if -else 语句

if - elif - else 语句
格式：
if 表达式1:
    语句1
elif 表达式2:
    语句2
elif 表达式3:
    语句3

...
elif 表达式n:
    语句n
else:      可有可无
    语句e

    逻辑：当程序执行if-elif-else语句时，首先计算“表达式1”的值，如果表达式1的值为真，则执行语句1，
    执行完语句1，则跳过真个if-elif-esle语句。如果表达式1的值为假，计算“表达式2”的值，
    如果表达式2的值为真，则执行语句2，执行完语句2，则跳过真个if-elif-esle语句.如此下去直到某个
    表达式为真，才停止，如果没有一个真的表达式，且有else，则执行语句e。

'''

age = int(input())
if age < 0 :
    print("娘胎里")
elif age >=0 and age <=3:
    print("婴儿")
elif age >=4 and age <=6:
    print("儿童")
elif age >=7 and age <=18:
    print("童年")
elif age >=19 and age <=30:
    print("青年")
elif age >=31 and age <=40:
    print("壮年")
elif age >=7 and age <=18:
    print("童年")
elif age >=41 and age <=50:
    print("中年")
else:
    print("老年")
#每个elif都是对它上面所有表达式的否定



