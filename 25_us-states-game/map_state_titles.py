from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "bold")

class StateTitles(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.list = []

    def display_state_title(self, state_title, x_coordinate, y_coordinate):
        state = Turtle()
        state.hideturtle()
        state.penup()
        state.color("black")
        state.goto(x_coordinate, y_coordinate)
        state.write(state_title, align=ALIGNMENT, font=FONT)
        self.list.append(state)



