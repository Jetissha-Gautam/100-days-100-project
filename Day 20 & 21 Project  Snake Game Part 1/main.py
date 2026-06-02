from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600,height=600)
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

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

    if snake.body[0].xcor()>280 or snake.body[0].xcor()<-280 or snake.body[0].ycor()>280 or snake.body[0].xcor()<-280:
        ON=False
        scoreboard.game_over()

    if snake.body[0].distance(food)<25:
        snake.add_body(food.color()[0])     
        food.new_food() 
        scoreboard.increase() 
        
    for blocks in snake.body[1:]:
    
        if snake.body[0].distance(blocks)<10:
            ON=False
            scoreboard.game_over()

screen.exitonclick()