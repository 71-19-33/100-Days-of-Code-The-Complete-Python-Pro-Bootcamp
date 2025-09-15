from turtle import Screen
from user_turtle import UserTurtle
from scoreboard import Scoreboard
from car import Traffic
import time

#Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

#Object setup
user_turtle = UserTurtle()
level_board = Scoreboard()
traffic = Traffic()
screen.update()

#Listeners
screen.listen()
screen.onkey(user_turtle.move, "Up")

#Game sequence
game_running = True

while game_running:
    time.sleep(0.1)
    traffic.move()
    screen.update()

    if user_turtle.ycor() > 260:
        level_board.increase_level()
        traffic.increase_speed()
        user_turtle.return_to_start()

    for car in traffic.car_list:
        if user_turtle.distance(car) < 10:
            game_running = False
            level_board.game_over()

#Exit on click
screen.exitonclick()