from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

#Screen setup
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

#Snake setup
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

#Listener
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Game sequence
game_running = True

while game_running:
    #Screen refresh logic
    screen.update()
    snake.move()

    #Detect collision with food
    if snake.body[0].distance(food) < 20:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    #Detect collision with wall
    if snake.body[0].xcor() > 280 or snake.body[0].xcor() < -280 or snake.body[0].ycor() > 280 or snake.body[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail.
    for segment in snake.body[1:]:
        if snake.body[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

#Exit on click
screen.exitonclick()