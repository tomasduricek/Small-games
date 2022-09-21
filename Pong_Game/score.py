from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 30, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.score_r = 0
        self.score_l = 0
        self.penup()
        self.goto(0, 250)

    def score(self):
        self.write(f'{self.score_l}       {self.score_r}', align='center', font=FONT)

    def score_up_r(self):
        self.score_r += 1

    def score_up_l(self):
        self.score_l += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)
