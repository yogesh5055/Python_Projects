from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,220)
        self.show_score()
    def update(self):
        self.score+=1
        self.clear()
        self.show_score()
    def show_score(self):
        self.write(f"Score : {self.score}",align="center",font=(25)) 

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=(30))
