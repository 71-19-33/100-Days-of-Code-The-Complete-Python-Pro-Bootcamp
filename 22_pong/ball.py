from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_pace = 10
        self.y_pace = 10

    def move(self, heading):
        time.sleep(0.1)
        self.setheading(heading)
        self.goto(self.xcor()+self.x_pace, self.ycor()+self.y_pace)

    def bounce_wall(self):
        self.y_pace *= -1


    def bounce_paddle(self):
        self.x_pace *= -1.05
        self.y_pace *= 1.05