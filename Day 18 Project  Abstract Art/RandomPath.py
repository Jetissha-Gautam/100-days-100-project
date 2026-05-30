from turtle import Turtle,Screen
from random import choice,random,uniform
tim= Turtle()

tim.shape('classic')
tim.pensize(10)
def right():
    tim.right(90)
    #forward()
def left():
    tim.left(90)
    #backward()
def forward():
    tim.forward(100)
def backward():
    tim.backward(100)
def circle():
    radius=uniform(0,100)
    angle=uniform(0,360)
    tim.circle(radius,angle)
movement=[right,left,forward,backward,circle]
for _ in range(100):
    r=random()
    b=random()
    g=random()
    tim.color(r,g,b)
    choice(movement)()
screen=Screen()
screen.setup(width=1.0, height=1.0)
screen.exitonclick()
