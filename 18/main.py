import turtle
import random

#Initialization of the cursor
cursor = turtle.Turtle()
cursor.shape("classic")
cursor.color("magenta")
#cursor_color_palette = ["red", "green", "blue", "yellow", "orange", "purple", "black", "grey"]
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

#Task: Draw a square
#for i in range(4):
    #cursor.forward(100)
    #cursor.right(90)

#Task: Draw a dashed line
# for i in range (10):
#     cursor.pendown()
#     cursor.forward(5)
#     cursor.penup()
#     cursor.forward(5)

#Task: Draw shapes
# for i in range (3, 10):
#     cursor.color(random.choice(cursor_color_palette))
#     for j in range (i):
#         cursor.forward(100)
#         cursor.right(360/i)

#Task: Draw a random walk, with bigger line size
cursor.speed(11)
cursor.pensize(1)
# for i in range(100):
#     #cursor.pencolor(random.choice(cursor_color_palette))
#     cursor.color(random_color())
#     cursor.left(90*random.randint(0, 3))
#     cursor.forward(50)
for i in range(0, 359, 5):
    cursor.setheading(i)
    cursor.color(random_color())
    cursor.circle(150)

#Screen class and exit on screen method
screen = turtle.Screen()
screen.exitonclick()