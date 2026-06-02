from turtle import Turtle
import random

class Snake:
    
    def __init__(self):

        self.body=[]

        for i in range(3):

            t=Turtle(shape="circle")
            t.penup()    
            t.color(random.random(),random.random(),random.random())
            t.goto(-i*20,0)
            
            self.body.append(t)

    def move(self):

        for i in range(len(self.body)-1,0,-1):
            self.body[i].goto(self.body[i-1].pos())
        self.body[0].forward(20)

    def turn_right(self):
        if self.body[0].heading()!=180:
            self.body[0].setheading(0)
        
    def turn_left(self):
        if self.body[0].heading()!=0:
            self.body[0].setheading(180)    

    def turn_Up(self):
        if self.body[0].heading()!=270:
            self.body[0].setheading(90)
        
    def turn_Down(self):
        if self.body[0].heading()!=90:
            self.body[0].setheading(270)

    def add_body(self,color):
        t=Turtle(shape="circle")
        t.penup()    
        t.color(color)
        t.goto(self.body[-1].position())            
        self.body.append(t)