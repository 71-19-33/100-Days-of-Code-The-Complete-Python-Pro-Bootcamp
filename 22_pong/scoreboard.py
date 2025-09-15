from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 30, 'bold')

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(position)
        self.update()

    def update(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

positions = [(0,0), (0, 50), (0, 100), (0, 150), (0, 200), (0, 250), (0, -50), (0, -100), (0, -150), (0, -200), (0, -250)]

class DashedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.draw()

    def draw(self):
        for position in positions:
            bar = Turtle()
            bar.color("white")
            bar.shape("square")
            bar.penup()
            bar.shapesize(stretch_len=0.25) #5px len
            bar.goto(position)