from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('turtle')
        self.penup()
        self.goto(0,-280)
        self.left(90)
        self.move = 10

    def up(self):
       y_axis =  self.ycor() + self.move
       self.goto(self.xcor(),y_axis)

    def down(self):
        y_axis = self.ycor() - self.move
        self.goto(self.xcor(), y_axis)

    def player_right(self):
        x_axis = self.xcor() + self.move
        self.goto(x_axis,self.ycor())

    def player_left(self):
        x_axis = self.xcor() - self.move
        self.goto(x_axis,self.ycor())

    def refresh(self):
        self.goto(0,-280)
