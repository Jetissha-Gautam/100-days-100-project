from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

ON=True

screen=Screen()
screen.setup(height = 600 , width =800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

rp=Paddle((350,0))
lp=Paddle((-350,0))
ball=Ball()

screen.listen()
screen.onkey(rp.go_up,"Up")
screen.onkey(rp.go_down,"Down")
screen.onkey(lp.go_up,"w")
screen.onkey(lp.go_down,"s")

while ON:

    time.sleep(0.1)
    ball.move()    
    screen.update()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    
    if ball.xcor()>320 and ball.distance(rp)<50:
        ball.hit()
        
    if ball.xcor()<-320 and ball.distance(lp)<50:
        ball.hit()
    
screen.exitonclick()