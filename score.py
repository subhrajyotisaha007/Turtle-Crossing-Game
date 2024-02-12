from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-250, 280)
        self.write(f'level: {self.level}',align='center',font=('Courier',10,'normal'))

    def lv(self):
        self.level += 1

    def game_over(self):
        self.clear()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write('Game Over',align='center',font=('Courier',50,'normal'))