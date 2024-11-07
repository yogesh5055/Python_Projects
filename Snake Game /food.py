from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        x=random.randint(-240,240)
        y=random.randint(-240,240)
        self.goto(x,y)
    def refresh(self):
         x=random.randint(-240,240)
         y=random.randint(-240,240)
         self.goto(x,y)
