from turtle import Turtle
from random import choice,randint

COLOUR = ['red','green','blue','yellow']
X_AXIS = 300
MOVE = 10
class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.car_all = []
        self.car_speed = 10


    def car_gen(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLOUR))
            new_car.goto(X_AXIS, randint(-250, 250))
            self.car_all.append(new_car)

    def move(self):
        for single_car in self.car_all:
            x_axis = single_car.xcor() - self.car_speed
            single_car.goto(x_axis, single_car.ycor())

    def level_up(self):
        self.car_speed += MOVE
