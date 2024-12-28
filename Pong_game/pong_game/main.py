from turtle import Screen,Turtle
from poddle import Poddle
from scoreboard import Scoreboard
from ball import Ball
import time
screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = Poddle(350,0)
l_paddle = Poddle(-350,0)
ball = Ball()
score_x = Scoreboard(60,260,"Left")
score_y = Scoreboard(-60,260,"Right")
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"s")
screen.onkey(l_paddle.go_down,"x")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()<-280 or ball.ycor()>280:
        ball.check_bounce_y()
    # detect colloison with right paddle
    if ball.distance(r_paddle)<50 and ball.xcor()> 320 or ball.distance(l_paddle)<50 and ball.xcor()< -320:
        ball.check_bounce_x()
    #  detect colloison with left paddle
    if ball.xcor() > 370:
        ball.reset_position()
        score_y.increase_score()
        if score_y.score == 5:
            score_y.game_over()
            game_is_on = False
    if ball.xcor() < -370:
        ball.reset_position()
        score_x.increase_score()
        if score_x.score == 5:
            score_x.game_over()
            game_is_on = False

        



























screen.exitonclick()