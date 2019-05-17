#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
简单的绘图工具
提供一个小海龟，可以把它理解为一个机器人，只能听得懂有限的命令

绘图窗口的原点（0，0）在正中间，默认的海龟的方向朝右

运动命令
forward(d) 向前运动长度
backward(d) 向后运动长度
right(d) 向右转动多少度
left(d) 向左转动多少度
goto(x,y) 移动到坐标（x，y）的位置
speed() 笔画绘制的速度[0,10]

笔画控制命令
up() 笔画抬起，在移动的时候不会绘图
down() 笔画落下，移动绘图
setheading(d) 改变海龟的方向
pensize(d) 笔画的宽度
pencolor() 笔画的颜色
reset() 回复多有设置，清空窗口，重置turtle状态
clear()清空窗口，不会重置turtle
circle(r,e) r代表圆的半径，e代表次数

begin_fill()
fillcolor
end_fill()
其他命令
done() 程序继续执行
undo() 撤销上一次动作
hideturtle() 隐藏海龟
showturtle() 显示海龟
screensize(x,y)



'''









#导入 turtle
import turtle

turtle.forward(50)
turtle.goto(100,50)
turtle.circle(100)
turtle.goto(-100,50)
turtle.circle(100)
turtle.begin_fill()
turtle.fillcolor('red')
turtle.end_fill


turtle.done()