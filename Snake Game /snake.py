from turtle import Turtle
MOVE=[(0,0),(-20,0),(-40,0)]
DISTANCE=20

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:  
    def __init__(self):
        self.snakes=[]
        self.create_snake()

    def create_snake(self):
        for i in MOVE:
            self.add_snake(i)


    def add_snake(self,position):
            snake = Turtle()
            snake.shape("square")
            snake.color('white')
            snake.penup()
            snake.goto(position)
            self.snakes.append(snake)
    def extend(self):
        self.add_snake(self.snakes[-1].position())
        
        
   
    
    def move(self):
           for i in range(len(self.snakes)-1,0,-1):
            x=self.snakes[i-1].xcor()
            y=self.snakes[i-1].ycor()
            self.snakes[i].goto(x,y)
            self.snakes[0].forward(0)
           self.snakes[0].forward(DISTANCE)
    def up(self):
        if self.snakes[0].heading() != DOWN:
          self.snakes[0].setheading(UP)
    def down(self):
         if self.snakes[0].heading() != UP:
           self.snakes[0].setheading(DOWN)
    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)
    def right(self):
        if self.snakes[0].heading() != LEFT:  
           self.snakes[0].setheading(RIGHT)

  
    

  

        

