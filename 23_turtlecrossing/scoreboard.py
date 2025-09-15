from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(x=-280, y=260)
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align='Center', font=("Courier", 36, "bold"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update()