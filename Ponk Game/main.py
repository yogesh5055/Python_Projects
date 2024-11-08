from turtle import Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Score
import time

r_paddle = Paddle(380)
l_paddle = Paddle(-380)
ball = Ball()
score=Score()
screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_over = False

while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

   
    if ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle.paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if  ball.xcor() > 380:
        ball.reset_postion()
        score.l_point()
        
    if  ball.xcor() < -380:
        ball.reset_postion()
        score.r_point()
     
        


screen.exitonclick()
