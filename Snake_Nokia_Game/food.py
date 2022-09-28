from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('black')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_food_x_location = random.randint(-280, 280)
        random_food_y_location = random.randint(-280, 280)
        self.goto(random_food_x_location, random_food_y_location)
