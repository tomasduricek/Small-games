from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('black')
        self.speed('fastest')
        self.goto(0, 0)
        self.xcor()
        self.x = 10
        self.y = 10

    def move_ball(self):
            new_y = self.ycor() + self.x
            new_x = self.xcor() + self.y
            self.goto(new_x, new_y)

    def bounce_y(self):
        self.x *= -1

    def bounce_x(self):
        self.y *= -1
