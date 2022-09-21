from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto((STARTING_POSITION))
        self.shape('turtle')
        self.setheading(90)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('black')


    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
