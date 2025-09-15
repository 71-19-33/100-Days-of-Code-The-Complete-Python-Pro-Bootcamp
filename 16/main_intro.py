#from turtle import Turtle, Screen
#my_turtle = Turtle()
#my_turtle.shape("turtle")
#my_turtle.color("DarkGoldenrod")
#my_turtle.forward(100)
#my_screen = Screen()
#my_screen.exitonclick()

from prettytable import PrettyTable
my_table = PrettyTable()
my_table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
my_table.add_column("Type",["Electric","Water","Fire"])
my_table.align = "l"

print(my_table)