from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        with open('highscore.txt') as file:
            self.highscore = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self.score} High score: {self.highscore}', align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.write_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.clear()
        self.write_score()
        with open('highscore.txt', mode='w') as file:
            file.write(f'{self.highscore}')

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f'GAME OVER, YOUR SCORE IS {self.score}', align=ALIGNMENT, font=FONT)
