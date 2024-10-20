from turtle import Turtle,Screen
import random
import colorgram
screen=Screen()
screen.colormode(255)
my_turtle=Turtle()
colors = colorgram.extract('Untitled.jpeg', 30)
color_list = []
my_turtle.penup()
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)
my_turtle.speed("fastest")
my_turtle.setheading(255)
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dots=100
for dot_count in range(1,number_of_dots+1):
   my_turtle.dot(20,random.choice(color_list))
   my_turtle.forward(50)
   if dot_count % 10 == 0:
       my_turtle.setheading(90)
       my_turtle.forward(50)
       my_turtle.setheading(180)
       my_turtle.forward(500)
       my_turtle.setheading(0)
screen.exitonclick()


