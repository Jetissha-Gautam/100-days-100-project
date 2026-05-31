from turtle import Turtle ,Screen
tim=Turtle()
screen=Screen()
def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_anticlockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clearscreen():
    tim.clear()
    
screen.listen()
screen.onkey(move_forwards,"w") 
screen.onkey(move_backwards,"s") 
screen.onkey(move_anticlockwise,"a") 
screen.onkey(move_clockwise,"d") 
screen.onkey(clearscreen,"c") 

screen.exitonclick()