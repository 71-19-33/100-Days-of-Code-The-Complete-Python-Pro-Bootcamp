from turtle import Turtle

PACE = 20
START_POSITION = (0, -270)

class UserTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.return_to_start()

    def return_to_start(self):
        self.goto(START_POSITION)

    def move(self):
        self.forward(PACE)