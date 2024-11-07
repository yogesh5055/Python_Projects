from turtle  import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

screen=Screen()

screen.setup(width=500,height=500)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_over=False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update()
    if snake.snakes[0].xcor() > 240 or snake.snakes[0].xcor() <-240 or snake.snakes[0].ycor() > 240 or snake.snakes[0].ycor() < -240 :
        game_over=True
        score.game_over()

    for i in snake.snakes:
        if i == snake.snakes[0]:
            pass
        elif snake.snakes[0].distance(i) < 10:
            game_over=True
            score.game_over()

screen.mainloop()
