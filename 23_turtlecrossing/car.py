from turtle import Turtle
import random

COLORS = ('blue', 'green', 'yellow', 'red', 'purple', 'orange')
X_POSITION_REGULAR = 320
Y_MIN = -240
Y_MAX = 260
START_SPEED = 5

AMOUNT_OF_CARS = 25

class Traffic(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []
        self.speed = START_SPEED
        self.start_traffic()

    def spawn_car(self, x_position):
        car = Turtle(shape='square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.goto(x=x_position, y=random.randint(Y_MIN, Y_MAX))
        self.car_list.append(car)

    def start_traffic(self):
        for i in range(AMOUNT_OF_CARS):
            x_position_start = random.randint(-280, 280)
            self.spawn_car(x_position_start)

    def move(self):
        for car in self.car_list:
            car.goto(car.xcor()-self.speed, car.ycor())
            if car.xcor() < -320:
                self.car_list.remove(car)
                self.spawn_car(X_POSITION_REGULAR)

    def increase_speed(self):
        self.speed *= 1.25
