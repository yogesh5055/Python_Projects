from turtle import Turtle
class Paddle:
    def __init__(self,position):
             self.paddle=Turtle()
             self.paddle.shape("square")
             self.paddle.color("white")
             self.paddle.shapesize(5,1)
             self.paddle.penup()
             self.paddle.goto(position,0)

    def go_up(self):
        y=self.paddle.ycor()+20
        self.paddle.goto(self.paddle.xcor(),y)
    def go_down(self):
        y=self.paddle.ycor()-20
        self.paddle.goto(self.paddle.xcor(),y)
    def xcor(self):
        return self.paddle.xcor()

    def ycor(self):
        return self.paddle.ycor()

    
