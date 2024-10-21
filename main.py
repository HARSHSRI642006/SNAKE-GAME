from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("My Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor ("black")
screen.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        board.increase()
    if snake.head.xcor()<-280 or snake.head.xcor()>280  or snake.head.ycor()>280 or snake.head.ycor()<-280 :
        game = False
        board.gameover()      
    for segemnt in snake.segment[1:]:
       
        if snake.head.distance(segemnt)<10:
            game = False
            board.gameover()

screen.exitonclick()    