from turtle import Turtle
class Middle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.color('black')
        for i in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)