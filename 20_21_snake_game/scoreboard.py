from turtle import Turtle

X_POSITION = 0
Y_POSITION = 270
COLOR = "green"
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

with open("highscore.txt") as file_read:
    highscore = file_read.read()
    if highscore == "":
        highscore = 0
    print(highscore)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.goto(x=X_POSITION, y=Y_POSITION)
        self.hideturtle()
        self.score = 0
        self.high_score = highscore
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("highscore.txt", 'w') as file_write:
                file_write.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 36, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()