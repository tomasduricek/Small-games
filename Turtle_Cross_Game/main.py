import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('ghost white')
player = Player()
screen.setup(width=600, height=600)

screen.tracer(0)
screen.listen()
screen.onkey(player.move, 'Up')

car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.game_score()
    car_manager.create_car()
    car_manager.move_cars()
    if player.ycor() == 300:
        player.goto((0, -280))
        scoreboard.score_up()
        scoreboard.clear()
        scoreboard.game_score()
        car_manager.MOVE_INCREMENT =+ 5
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            time.sleep(2)
            screen.clear()
            scoreboard.game_over()
            time.sleep(3)
            game_is_on = False
