import colorgram
import turtle
import random
def go(i):
    for j in range(i):
        x=random.choice(colors)
        t.pencolor(x.rgb.r,x.rgb.g,x.rgb.b)
        t.forward(1)
        t.penup()
        t.forward(50)
        t.pendown()

t=turtle.Turtle()
colors = colorgram.extract(
    r"G:\My Drive\Colab Notebooks\100 Days 100 Projects\Day 18 Project  Hirst Painting\image.jpg",
    500
)
t.pensize(20)
screen=turtle.Screen()
screen.colormode(255)
t.hideturtle()
t.penup()
t.setpos(-600,400)
t.pendown()
for i in range (5):    
    go(9)
    t.right(90)
    go(1)
    t.right(90)
    go(9)
    t.left(90)
    go(1)
    t.left(90)
    
screen.exitonclick()