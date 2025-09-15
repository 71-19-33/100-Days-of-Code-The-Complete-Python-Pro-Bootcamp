from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, DashedLine
import random

#TODO1: Create screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#TODO2: Create and move paddle
paddle_left = Paddle((-350, 0))
#TODO3: Create another paddle
paddle_right = Paddle((350, 0))
#TODO4: Create the ball and make it move
ball = Ball()

score_right = Scoreboard((200, 200))
score_left = Scoreboard((-200, 200))

separator = DashedLine()

#Listener
screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

#game sequence
game_running = True
ball_heading = random.randint(0, 359)
while game_running:
    screen.update()
    ball.move(ball_heading)

    # TODO5: Detect collision with ball and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    #TODO6: Detect collision with paddle
    if ball.distance(paddle_right) < 20 and ball.xcor() > 320 or ball.distance(paddle_left) < 20 and ball.xcor() < -320:
        ball.bounce_paddle()

    #TODO7: Detect when ball goes out of bounds
    #TODO8: Keep score
    if ball.xcor() > 380:
        ball.goto(0, 0)
        score_left.increase_score()

    if ball.xcor() < -380:
        ball.goto(0, 0)
        score_right.increase_score()

#Exit on click
screen.exitonclick()