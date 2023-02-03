from turtle import Turtle


class Answer(Turtle):

    def __init__(self, x, y, state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(state)
