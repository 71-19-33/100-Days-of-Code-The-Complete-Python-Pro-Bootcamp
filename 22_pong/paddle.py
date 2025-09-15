from turtle import Turtle

UP = 90
DOWN = 270
PACE = 50

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() <= 250-PACE:
            self.goto(self.xcor(), self.ycor()+PACE)

    def move_down(self):
        if self.ycor() >= -250+PACE:
            self.goto(self.xcor(), self.ycor()-PACE)