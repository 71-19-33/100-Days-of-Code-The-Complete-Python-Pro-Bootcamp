import colorgram, random, turtle

#Extract colors from attached image file and store as tuples in list
extracted_colors = colorgram.extract("image.jpg", 20)
colors = []
for entry in extracted_colors:
    colors.append(tuple(entry.rgb))

#Set up turtle
turtle.colormode(255)
cursor = turtle.Turtle()

#Set up turtle cursor
cursor.hideturtle()
cursor.speed(11)

#Initialize cursor position
x_pos = -250
y_pos = -250
cursor.penup()
cursor.setpos(x_pos, y_pos)

#Draw Hirst painting in a 10x10 grid, 20 size dots, spaced apart 50 size
for i in range(10):
    cursor.setpos(x_pos, y_pos+(50*i))
    for j in range(10):
        cursor.color(random.choice(colors))
        cursor.pendown()
        cursor.dot(20)
        cursor.penup()
        cursor.forward(50)

#Screen class and exit on screen method
screen = turtle.Screen()
screen.exitonclick()