import turtle
from turtle import Turtle,Screen
import random

t1=Turtle(shape="turtle")
t2=Turtle(shape="turtle")
t3=Turtle(shape="turtle")
t4=Turtle(shape="turtle")
t5=Turtle(shape="turtle")
t6=Turtle(shape="turtle")
t7=Turtle(shape="turtle")

players=[t1,t2,t3,t4,t5,t6,t7]

screen=Screen()

# colors = [
#     (255, 0, 0),      # Red
#     (255, 165, 0),    # Orange
#     (255, 255, 0),    # Yellow
#     (0, 255, 0),      # Green
#     (0, 0, 255),      # Blue
#     (128, 0, 128),     # Purple
#     (255, 192, 203)  # Pink
# ]
colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink"
]

screen.setup(500,400)

ON=False
bet=screen.textinput("Make your bet","Who do you think will win the race? (red,orange,yellow,green,blue,purple,pink)").lower()
ON=True
for i,t in enumerate(players) :
    
    t.color(colors[i])
    t.penup()
    t.goto(-230,-150+(i*50))

while ON:
        
    for t in players:

        distance=random.randint(0,20)
        t.forward(distance)

        if t.xcor()>230:
            
            win=t.pencolor()
            
            if win==bet:

                t.goto(0,0)
                t.write(
                    "YOU WON !!! ",
                    align="center",
                    font=("monospace", 20, "normal")
                )
                
                
            else:

                t.goto(0,0)
                t.write(
                    "YOU LOSE !!! ",
                    align="center",
                    font=("monospace", 20, "normal")
                )
                
            ON=False
            break

print(f"{win} won the race")
screen.exitonclick()