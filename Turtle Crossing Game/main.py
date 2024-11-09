import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car_manger=CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(player.move,"Up")







game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manger.create_car()
    car_manger.move_cars()

    for car in car_manger.all_cars:
        if car.distance(player) < 20:
               game_is_on=False
               score.game_over()
               
               
    if player.is_it_finish_line():
         player.go_to_start()
         car_manger.level_up()
         score.increase()
    
screen.exitonclick()