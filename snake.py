starting_position = [(-60,20),(-20,10),(-40,20)]
from turtle import Screen,Turtle
move_dist = 20
up = 90
down = 270
left = 180
right = 0
class Snake:

 
 
 
 
 def __init__(self):
    
  self.segment = []
  self.create_snake()
  self.head = self.segment[0]
 def create_snake(self):
   for value in starting_position: 
    self.add_segment(value)
 def add_segment(self,value): 
    tim_1 = Turtle()
    tim_1.shape("square")

    tim_1.color("white")
    tim_1.penup()
    tim_1.goto(value)
    self.segment.append(tim_1) 
 def extend(self):
   self.add_segment(self.segment[-1].position())

 

 def move(self):
     
    for seg_num in range (len(self.segment)-1,0, -1):
     new_x = self.segment[seg_num-1].xcor()
     new_y = self.segment[seg_num-1].ycor()
     self.segment[seg_num].goto(new_x,new_y)
    self.segment[0].forward(move_dist)  

 

 def up(self):
   if self.head.heading()!= down:
    self.head.setheading(up)
 def down(self):
   if self.head.heading()!= up:
    self.head.setheading(down)  
 def left(self):
   if self.head.heading()!= right:
    self.head.setheading(left)  
 def right(self):
   if self.head.heading()!= left:
    self.head.setheading(right)
     
        






