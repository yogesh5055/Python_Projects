from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    def move(self):
        self.forward(MOVE_DISTANCE)
    def is_it_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False    



