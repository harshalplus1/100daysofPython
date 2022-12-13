import colorgram
from turtle import Turtle,Screen
import random
colors=colorgram.extract('img.jpg',25)
col=colors[0]
s=Screen()
t=Turtle()
s.colormode(255)
cols=[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    nc=(r,g,b)
    cols.append(nc)

t.pensize(20)
t.penup()
t.setx(-350)
t.sety(300)
for i in range(16):
    for j in range(18):
        t.pencolor(cols[random.randint(0,24)])
        t.pendown()
        t.forward(1)
        t.penup()
        t.forward(40)
    t.back(738)
    t.right(90)
    t.forward(40)
    t.left(90)


t.forward(1)
s.exitonclick()
