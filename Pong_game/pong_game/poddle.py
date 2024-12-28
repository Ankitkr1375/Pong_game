from turtle import Turtle
class Poddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x,y)

    def go_up(self):
        if self.ycor() <= 230:
            self.new_y = self.ycor()+40
            self.goto(self.xcor(),self.new_y)
    def go_down(self):
        if self.ycor() >= -230:
            self.new_y = self.ycor()-40
            self.goto(self.xcor(),self.new_y)
