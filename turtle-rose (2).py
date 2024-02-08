# import math
# import turtle
# import time

# turtle.bgcolor("black")
# turtle.shape("turtle")
# turtle.speed(0)
# turtle.fillcolor("brown")
# phi = 137.508 * (math.pi / 180.0)

# for i in range (160 + 40):
#     r = 4 * math.sqrt(i)
#     theta = 4 * phi
#     x= r * math.cos(theta)
#     y = r * math.sin(theta)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.setheading(i * 137.508)
#     turtle.pendown()
#     if i < 160:
#         turtle.stamp()
#     else:
#         turtle.fillcolor("yellow")
#         turtle.begin_fill()
#         turtle.right(20)
#         turtle.forward(70)
#         turtle.left(40)
#         turtle.forward(70)
#         turtle.left(140)
#         turtle.forward(70)
#         turtle.left(40)
#         turtle.forward(70)
#         turtle.end_fill()
# turtle.hideturtle()

# time.sleep(20)

from turtle import *
from math import *
import time

speed(0)
bgcolor("black")
goto(0,-40)

for i in range(16):
    for j in range(18):
        color('#0D52BD')
        rt(90)
        circle(150-j*6,90)
        lt(90)
        circle(150-j*6,90)
        rt(180)
    circle(40,24)

color("black")
shape("circle")
shapesize(0.5)
fillcolor('#FFFF00')
golden_angle=137.508
phi = golden_angle*(pi/180)

for i in range(110):
    r = 4 *sqrt(i)
    theta = i*phi
    x=r*cos(theta)
    y=r*sin(theta)
    penup()
    goto(x,y)
    setheading(i*golden_angle)
    pendown()
    stamp()

time.sleep(50)