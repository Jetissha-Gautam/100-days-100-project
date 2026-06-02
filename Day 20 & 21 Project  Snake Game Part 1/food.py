from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize()
        self.color(random.random(),random.random(),random.random())
        self.speed("fastest")
        self.goto(random.randint(-280,280),random.randint(-280,280))
    
    def new_food(self):
        self.color(random.random(),random.random(),random.random())
        self.goto(random.randint(-280,280),random.randint(-280,280))