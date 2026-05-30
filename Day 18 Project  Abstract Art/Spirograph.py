from turtle import Turtle,Screen
from random import random
t=Turtle()
t.speed(100)
for  i in range(36):
    r=random()
    b=random()
    g=random()
    t.color(r,g,b)
    t.circle(100)
    current_heading=t.heading()
    t.setheading(current_heading+10)
s=Screen()
s.exitonclick()