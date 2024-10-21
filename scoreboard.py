from turtle import Turtle


ALIGNEMNT = "center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
     
        
     super().__init__()
     self.score = 0
     self.color("white")
     self.penup()
     self.goto(0,270)
     
     
     self.hideturtle()
     self.update()

    def update(self): 
       self.write(f"Score:{self.score}",align=ALIGNEMNT,font=FONT)
    def gameover(self):
       self.goto(0,0)
       self.write("GAME OVER",align=ALIGNEMNT,font=FONT)
    def increase(self) :
       self.score+=1
       self.clear()
       self.update()



     

    