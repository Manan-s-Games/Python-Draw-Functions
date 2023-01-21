from turtle import *
import random
bgcolor('black')
speed(0)
hideturtle()
i = 0
while True:
    pencolor("red")
    circle(i)
    pencolor('orange')
    circle(i * 0.8)
    right(3)
    forward(3)
    i+=1