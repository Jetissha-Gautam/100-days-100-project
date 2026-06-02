from turtle import Screen
import time
from snake import Snake

screen=Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600,height=600)
screen.tracer(0)

snake=Snake()
ON=True

while ON:

    screen.update()
    time.sleep(0.1)

    snake.move()

    screen.listen()
    screen.onkey(snake.turn_right,"Right") 
    screen.onkey(snake.turn_left,"Left") 
    screen.onkey(snake.turn_Up,"Up") 
    screen.onkey(snake.turn_Down,"Down") 
        

screen.exitonclick()