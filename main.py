import time
from turtle import Screen
from player import Player
from car_manager import Cars
from score import Score


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(0)

cars = Cars()
player = Player()
score = Score()

screen.listen()
screen.onkeypress(player.up,'Up')
screen.onkeypress(player.down,'Down')
screen.onkeypress(player.player_right,'Right')
screen.onkeypress(player.player_left,'Left')



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.car_gen()
    cars.move()
    for car in cars.car_all:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    if player.ycor() > 280:
        score.lv()
        score.update()
        player.refresh()
        cars.level_up()

screen.exitonclick()
