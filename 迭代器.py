#!/usr/bin/python
# -*- coding:utf-8 -*-
from collections import Iterable
from collections import Iterator
'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象
（iterable）可以用isinstance()去判断一个对象是否是iterable对象

可以直接作用于for的数据类型一般分为两种
1 集合数据类型，如 list tuple dict set string
2 是generator，包括生成器和带yield的generator function



'''


print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(1,Iterable))


'''
迭代器：不但可以作用于for循环，还可以被net()函数不断调用并返回下一值，直到最后跑出一个
StopItertation错误表示无法继续返回下一个值


可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator对象)

可以使用isinstance()函数判断一个对象是否是Iterator


'''

l1 = (x for x in [12,123,34,24])
print(next(l1))
print(next(l1))
print(next(l1))


print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance("",Iterator))
print(isinstance((x for x in range(10)),Iterator))



#转成Iterator 对象 iter()
a =iter([1,2,3,4,5,6])
print(next(a))
print(next(a))

