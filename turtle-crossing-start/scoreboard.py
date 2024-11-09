FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
      def __init__(self):
            self.level=1
            super().__init__()
            self.penup()
            self.hideturtle()
            self.goto(-200,250)
            self.update()
      def update(self):
            self.write(f"Level :{self.level}",align="center",font=FONT)      
      
      def increase(self):
            self.level+=1
            self.clear()
            self.update()
            
      def game_over(self):
            self.goto(0,0)
            self.write("GAME OVER",font=FONT,align="center")
            