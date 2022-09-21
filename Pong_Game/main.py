from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard
from middle_line import Middle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('white')
screen.title('Pong')
screen.tracer(0)

middle = Middle()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


ball = Ball()
score = Scoreboard()
game = True

while game:
    screen.update()
    time.sleep(0.05)
    ball.move_ball()
    score.score()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        score.score_up_r()
        score.clear()
        score.score()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        score.score_up_l()
        score.clear()
        score.score()
    if ball.xcor() > 400 or ball.xcor() < -400:
        game = False
        screen.clear()
        score.game_over()
        time.sleep(2)
        screen.clear()
        score.score()

game = True
while game:
    screen.update()
screen.exitonclick()
