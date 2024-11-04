import random
from turtle import Turtle,Screen
#Set up Screen Size
screen = Screen()
# Key word arguments
game_over=True

screen.setup(width=500,height=400)
user_choice=screen.textinput(title="Turtle Racing",prompt="Which turtle will win the race?\nEnter the color: ")

colors=['red','blue','orange','yellow','green','purple']
position=[-70,-40,-10,20,50,80]
turtles=[]

for color in range(0,5):
      t=Turtle(shape="turtle")
      t.color(colors[color])
      t.penup()
      t.goto(-250,position[color])
      turtles.append(t)

if user_choice:
      game_over=False

while not game_over:
      for turtle in turtles:
          if turtle.xcor()>230:
                game_over=True
                winning_color=turtle.pencolor()
                if winning_color==user_choice:
                      print(f"You've Won!\nThe winning color is: {winning_color}")
                else:
                      print(f"You've loss!\nThe winning color is: {winning_color}")
          distance = random.randint(0,10) 
          turtle.forward(distance)     

screen.exitonclick()

