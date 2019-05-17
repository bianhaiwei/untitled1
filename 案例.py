#!/usr/bin/python
# -*- coding:utf-8 -*-

endstr = 'end'
str = ""
for line in iter(input, endstr):
    str += line

print(str)