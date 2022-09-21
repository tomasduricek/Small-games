from turtle import Turtle


FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        self.penup()
        self.goto(0, 250)

    def game_score(self):
        self.goto(-250, 250)
        self.write(f'Level: {self.score}', align='left', font=FONT)

    def score_up(self):
        self.score+=1

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=FONT)



