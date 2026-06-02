from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.display()
    
    def display(self): 
        self.hideturtle()   
        self.goto(0,250)
        self.color("white")
        self.write(f"Score : {self.score}", align="center", font=("Courier", 24, "normal"))
    
    def increase(self):
        self.clear()
        self.score+=1
        self.display()

    def game_over(self):
        self.goto(0,0)
        self.color('white')
        self.write(f"GAME OVER ! \n Score : {self.score}", align="center", font=("Courier", 24, "normal"))
