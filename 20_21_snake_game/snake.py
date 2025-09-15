import turtle, time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.body = []
        self.draw()

    def draw(self):
        """Draws white squares, lifts the pen, positions the drawn square next to lastly created
        and stores the object in the provided body."""
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        square = turtle.Turtle(shape="square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.body.append(square)

    def reset(self):
        for segment in self.body:
            segment.goto(1000, 1000)
        self.body.clear()
        self.draw()

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        """ Moves object_list according to the move of the 0th object and updates the position of the rest according
         to the position of the previous element before movement."""
        time.sleep(0.1)
        for segment in range(len(self.body) -1, 0, -1):
            self.body[segment].goto(self.body[segment-1].xcor(), self.body[segment-1].ycor())
        self.body[0].forward(20)

    def up(self):
        """Move snake upwards."""
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def down(self):
        """Move snake downwards."""
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def left(self):
        """Move snake to the left."""
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def right(self):
        """Move snake to the right."""
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)