# import turtle
#
# #Set up turtle cursor
# cursor = turtle.Turtle()
# cursor.shape("classic")
#
# #On key functions
# def move_forward():
#     cursor.forward(15)
#
# def move_backward():
#     cursor.backward(15)
#
# def turn_clockwise():
#     cursor.right(15)
#
# def turn_anticlockwise():
#     cursor.left(15)
#
# def clear():
#     cursor.home()
#     cursor.clear()
#
# #Screen class
# screen = turtle.Screen()
#
# #Event listeners, on key
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_clockwise, "d")
# screen.onkey(turn_anticlockwise, "a")
# screen.onkey(clear, "c")
#
# #Exit on click method
# screen.exitonclick()