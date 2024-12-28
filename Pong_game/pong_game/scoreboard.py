from turtle import Turtle
GAMEOVER = ("Arial",24,"normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self,x,y,name):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.name  = name
        self.goto(x,y)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f" {self.score}",align="Center",font =("Courier",30,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER\n {self.name} Wins",align =ALIGNMENT,font = GAMEOVER)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
